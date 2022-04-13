from django.urls import path
from .views import about,contact, home, login, service, signup,add,update,delete

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('service/',service,name='service'),
    path('signup/',signup,name='signup'),
    path('add',add, name = 'add'),


    path('update/<int:id>', update, name = 'update'),
    path('delete/<int:id>', delete, name = 'delete')
]