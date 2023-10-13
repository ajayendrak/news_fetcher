from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
import logging
from .news_fetcher import news_fetcher_function
from user.models import *
from .models import *
from django.core.cache import cache
from user.serializers import *
from news.serializers import *

def home_view(request):
    return render(request, 'home.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

class FetchNewsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []
    # authentication_classes = []

    def post(self,request):
        try:
            keyword=request.data.get("keyword")
            sources=request.data.get("sources")
            from_date=request.data.get("fromdate")
            to_date=request.data.get("todate")
            language=request.data.get("language")
            category=request.data.get("category")
            today = datetime.today()
            refresh = request.data.get("refresh")
            print("----------22-------", refresh)
            user=request.user
            one_day_ago = today - timedelta(days=2)
            formatted_date = one_day_ago.strftime("%Y-%d-%m")
            print(request.data)
            if refresh:
                data = news_fetcher_function(query=keyword, sources=sources, from_date=from_date, to_date=to_date, language=language, category=category)
            else:
                cache_key = f"news_{keyword}_{category}_{language}_{from_date}_{to_date}_{sources}"
                cached_data = cache.get(cache_key)

                if cached_data is not None:
                    # If data is found in the cache, return it
                    return Response({
                        "status": "success",
                        'message': "Data fetched from cache",
                        'data': cached_data,
                    }, status=status.HTTP_200_OK)

                data = news_fetcher_function(query=keyword, sources=sources, from_date=from_date, to_date=to_date, language=language, category=category)
                cache.set(cache_key, data, 60 * 15)
            try:
                obj = UserKeywords.objects.get(user=user, keyword=keyword.strip())
            except Exception as e:
                obj = UserKeywords.objects.create(user=user, keyword=keyword.strip())
            try:
                if "articles" in data.keys():
                    if len(data["articles"]) == 0:
                        return Response({
                        "status":"error",
                        'message':"Data not found for given keyword",
                        'data' : data,
                    },status=status.HTTP_200_OK)
                sorted_articles = sorted(data["articles"], key=lambda x: x["publishedAt"], reverse=True)
                data["articles"] = sorted_articles
                return Response({
                        "status":"success",
                        'message':"Data fetched successfully",
                        'data' : data,
                    },status=status.HTTP_200_OK)
            except requests.exceptions.RequestException as e:
                print(e)
                return Response({'status':"fail", 'data':[], 'message':"Something went wrong please try again later"},status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(e)
            return Response({'status':"fail", 'data':[], 'message':"Something went wrong please try again later"},status.HTTP_500_INTERNAL_SERVER_ERROR)


class FetchKeywordsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []
    # authentication_classes = []

    def get(self,request):
        try:
            user = request.user
            objs = UserKeywords.objects.filter(user=user)
            data = UserKeywordsSerializers(objs, many=True).data
            return Response({
                        "status": "success",
                        'message': "Data fetched successfully",
                        'data': data,
                    }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'status':"fail", 'data':[], 'message':"Something went wrong please try again later"},status.HTTP_500_INTERNAL_SERVER_ERROR)