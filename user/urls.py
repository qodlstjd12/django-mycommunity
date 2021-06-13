
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'user'

urlpatterns=[
    path('register/', views.register, name = 'register'),
    path('login/', views.mylogin, name='login'),
    path('logout/',views.logout_view, name = 'logout'),
    path('', views.login_view, name='home')
]