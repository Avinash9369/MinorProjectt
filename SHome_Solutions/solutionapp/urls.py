from django.urls import path,include
from.import views,user_views
urlpatterns=[
    path("",views.home,name="home"),
    path("registration/",views.registration,name="registration"),
    path("login/",views.login,name="login"),
    path("feedback/",views.feedback,name="feedback"),
    path("query/",views.query,name="query"),
    path("about/",views.about,name="about"),
    path("user_home/",user_views.user_home,name="user_home"),
    path("user_feedback/",user_views.user_feedback,name="user_feedback"),
    path("user_logout/",user_views.user_logout,name="user_logout"),
    path("services/",views.services,name="services"),
    path("view_employee/<str:etype>/",views.view_employee,name="view_employee"),
    path("user_edit_profile/",user_views.user_edit_profile,name="user_edit_profile")
]  