from django.urls import path , include
from .api import ToDoViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',ToDoViewset)
urlpatterns = [
    path('api/' , include(router.urls)),
]
