from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('<str:id>', views.detail_view, name ='detail'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('user_delete/<str:id>',views.user_delete,name='user_delete'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('update/<str:id>', views.update, name='update'),
    path('message/', views.message_view, name = 'message_view'),
    path('comment/<str:id>',views.comment, name ='comment'),
    path('comment_delete/<str:id>,<str:id2>', views.comment_delete, name='comment_delete')
]