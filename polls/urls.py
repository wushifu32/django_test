from django.urls import path, re_path
from django.views.generic.base import RedirectView

from . import views

favicon_view = RedirectView.as_view(url='/static/polls/linux.ico', permanent=True)

app_name = 'polls'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    re_path(r'^favicon\.ico$', favicon_view),
    # 5/
    path('<int:pk>/', views.Details.as_view(), name='details'),
    # 5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
    # 5/results
    path('<int:pk>/results', views.Results.as_view(), name='results'),
]
