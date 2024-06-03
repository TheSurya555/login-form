from django.contrib import admin
from django.urls import path
from modellogin import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('signup/', views.signUp , name='signup'),
    path('login/', views.login_user , name='login'),
    path('about/', views.about_user , name='about'),
    path('logout/', views.user_logout , name='logout'),
    path('changepass/', views.changepass , name='changepass'),
    path('profile/', views.profile, name='profile'),
]
