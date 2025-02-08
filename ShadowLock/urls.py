from django.urls import path
from .views import *
urlpatterns = [
    path('', view=Home, name='home'),
    path('login/', view=login_view, name='login'),
    path('logout/', view=logout_view, name='logout'),
    path('dashboard/', view=Dashboard, name='dashboard'),
    path('passwords/', view=passwords, name='passwords'),
    path('environments/', view=environments, name='environments'),
    path('shared/', view=shared, name='shared'),
    path('passwords_create/', view=password_create_view, name='create_password')
]
