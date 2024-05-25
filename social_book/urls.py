"""social_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('home/',views.home, name='home'),
    path('upload_book/',views.upload_book, name='upload_book'),
    path('dash/',views.dashboard, name='dashboard'),
    path('allbooks/',views.allbooks, name='allbooks'),
    path('userBook/',views.uploaded_books, name='uploaded_books'),
    path('logout/', views.logout_view, name='logout'),
    path('display/', views.fetch_and_display, name='fetch_and_display'),
    #bulk data save from excel
    path('bulk/', views.bulkdata, name='bulkdata'),
    # Redirect to Tokens Apps Urls
    path('tokens/', include('tokens.urls')),
    # this is url
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media files on this position
