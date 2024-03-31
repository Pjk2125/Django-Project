from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientListCreate.as_view(), name='client-list'),
    path('clients/<int:pk>/', views.ClientRetrieveUpdateDestroy.as_view(), name='client-detail'),
    path('projects/', views.ProjectListCreate.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),
]
