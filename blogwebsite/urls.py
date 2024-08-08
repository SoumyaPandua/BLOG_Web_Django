"""
URL configuration for blogwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from authapp.views import *
from website.views import *
from adminpanel.views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('send-otp/', send_otp, name='send_otp'),
    path('', website, name="website"),
    path('post_blog/', post_blog, name='post_blog'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('forgot_password', forgot_password, name='forgot_password'),
    path('admin_dashboard/', admin_dash, name='admin'),
    path('admin/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('admin/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('manage_bloggers/', manage_bloggers, name="manage_bloggers"),
    path('manage_bloggers/edit/<int:blogger_id>/', edit_blogger, name='edit_blogger'),
    path('manage_bloggers/delete/<int:blogger_id>/', delete_blogger, name='delete_blogger'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)