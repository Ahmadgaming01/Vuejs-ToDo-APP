from django.urls import path , include
from .api import ToDoViewset
from .views import todo_list

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',ToDoViewset)
urlpatterns = [
    path('' , todo_list),
    path('api/' , include(router.urls)),
    
]
