from django.urls import path
from task_app import views

urlpatterns = [
    path('clients/', views.ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', views.ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-detail'),
    # path('projects/', views.ProjectListCreateAPIView.as_view(), name='project-list-create'),
    # path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]


