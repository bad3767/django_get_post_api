from . import views
from django.urls import path

urlpatterns = [
    path("",views.home,name='home'),
    path("data/",views.data,name='data'),
    path ("data/<int:id>",views.data_list,name='data_list'),
    path('update/<int:id>',views.update,name='update'),
    path("delete/<int:id>",views.delete,name='delete'),
    
]