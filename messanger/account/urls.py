from . import views
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.index, name='account'),
    path('myacc/', views.auth, name='myacc'),
    path('reg/', views.RegistrationView.as_view(), name='reg'),
]