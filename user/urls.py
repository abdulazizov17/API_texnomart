from django.urls import path
from user.views import RegisterApiView, UserLogoutApiView, UserLoginApiView
urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),


]