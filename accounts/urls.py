from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('signup/', views.signup, name='signup'),
] 