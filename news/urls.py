from django.urls import path,include
from news.views import *

urlpatterns = [
	path("fetch/", FetchNewsView.as_view(), name="news-fetch"),
	path("fetch/keywords/", FetchKeywordsView.as_view(), name="news-fetch-keywords"),
	]