from django.urls import path
from . import views

urlpatterns = [
    path('collects/',views.CollectListCreate.as_view(),name='collect_list'),
    path('collects/<int:pk>/',views.CollectRetrieveUpdateDestroy.as_view(),name='collect_detail'),

]