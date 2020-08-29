from django.urls import path
from book_app import views
urlpatterns=[
    path("login/",views.login), #登录功能的路由配置
    path("reg/",views.reg),
    path("reg2/",views.reg2),
    path("index/",views.index)
]