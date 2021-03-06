"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from tutorial.quickstart import views as quickstartviews
from tutorial.todoapp import views as todoviews
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users',quickstartviews.UserViewSet) #using viewsets url conf is auto generated from users
router.register(r'groups',quickstartviews.GroupViewSet) #using viewsets url conf is auto generated
router.register(r'todos',todoviews.TodoItemViewSet)#using viewsets url conf is auto generated

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# urlpatterns = [
#     path('', include(router.urls)),
#
# ]

urlpatterns = [
    path('todonew/', todoviews.TodoListAPIView.as_view()),
    path('todonew/<int:pk>/', todoviews.TodoDetailAPIView.as_view()),
    path('users/', todoviews.UserCreateAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
