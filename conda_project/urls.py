"""conda_project URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Conda import views



urlpatterns = [
    path('basic_home', views.basic, name="basic"),
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('more_project/',views.moreproject, name='more_project'),
    path('more_project_link/',views.moreprojectlink, name='more_project_link'),
    path('documentation_download_link/',views.documentation_download_link, name='documentation_download_link'),
    path('click_for_projects_ideas/',views.click_for_projects_ideas, name='click_for_projects_ideas'),
    path('Login_form/',views.Login_form, name='Login_form'),
    path('on_click_here_project/<int:id>',views.on_click_here_project, name = 'on_click_here_project'),
    path('small_login_form', views.Small_login_form, name="small_login_form"),
    path('PPT_Location', views.PPT_es, name="PPT"),

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
