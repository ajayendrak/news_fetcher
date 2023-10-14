from django.shortcuts import render
from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render


def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

def blocked_view(request):
    return render(request, 'blocked.html')

class UserSignUPView(APIView):
	permission_classes = []
	
	def post(self,request):
		try:
			serializer = UserSignUpSerializers(data=request.data)
			if serializer.is_valid():
				check_email = request.data.get('email')
				user=User.objects.filter(email=check_email).last()
				if user:
					return Response({'status':"fail", 'data':[], 'message':"User with provided email already exist in records"},status.HTTP_409_CONFLICT)
				else:
					user = serializer.save()
					user.set_password(serializer.data['password'])
					user.save()
					return Response({
						'status':'success','data':serializer.data,
						'message':"account created successfully."},status=status.HTTP_201_CREATED)
			else:
				return Response({'status':"fail", 'data':[], 'message':"provided email is not valid"},status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({'status':"fail", 'data':[], 'message':str(e)},status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLoginView(APIView):
	permission_classes = []
	def post(self,request):
		try:
			serializer = UserLoginSerializers(data=request.data)
			if serializer.is_valid(raise_exception=True):
				email = serializer.data.get("email")
				password = serializer.data.get('password')
				user = authenticate(email=email,password=password)
				
				if user is not None:
					if user.is_blocked:
						return Response({'status':"blocked", 'data':[], 'message':"User is blocked"},status.HTTP_200_OK)
					refresh = RefreshToken.for_user(user)
					user.extension_refresh=False
					user.save()
					return Response({
						"status":"success",
						"refresh":str(refresh),
						"access":str(refresh.access_token),
						'message':"account login successfully",
					},status=status.HTTP_200_OK)
				else:
					return Response({'status':"fail",'message':"Invalid Credentials"},status.HTTP_401_UNAUTHORIZED)
		except Exception as e:
			print(f'137-----------------{e}')
			return Response({'status':"fail", 'data':[], 'message':"something went wrong please try again later"},status.HTTP_500_INTERNAL_SERVER_ERROR)






