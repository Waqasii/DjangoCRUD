from django.conf.urls import url
from django.urls import path
from .views import * #CreateView,Store,index,viewEmployee

urlpatterns = [
    path('',index,name="index"),
    path('create',CreateView,name="create"),
    path('store',Store,name="store"),
    path('view/<int:pk>',viewEmployee,name="viewEmployee"),
    path('delete/<int:pk>',deleteEmployee,name="deleteEmployee"),
    path('update/<int:pk>',updateEmployee,name="updateEmployee"),
    path('edit/<int:pk>',update,name="update"),
]
