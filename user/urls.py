from django.urls import path,include
from user.views import *

urlpatterns = [
	path("signup/", UserSignUPView.as_view(), name="user-signup"),
	path("login/", UserLoginView.as_view(), name="user-login"),
	]