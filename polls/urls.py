from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # 5/
    path('<int:pk>/', views.Details.as_view(), name='details'),
    # 5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
    # 5/results
    path('<int:pk>/results', views.Results.as_view(), name='results'),
]
