from django.urls import path
from . import views

# urls pattren
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='aboutme'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('blog/',views.blogpost,name='blogpost'),
    path('blog/<str:Slug>/',views.blogposts,name='blogposts'),
    path('update/<str:Slug>/',views.update,name='update'),
    path('addpost/',views.addpost,name='addposts')
]