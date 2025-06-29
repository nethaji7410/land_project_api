from django.urls import path
from . import views
from .views import SavePositionView, ResetPositionView

urlpatterns = [
    path('tags/', views.TagListView.as_view()),  
    path('tags/<str:tag_name>/names/', views.DocumentNameListView.as_view()),
    path('positions/', views.SavePositionView.as_view()),
    path('positions/reset/', ResetPositionView.as_view()),
    path('auth/logout/', views.LogoutView.as_view()),  
]