from django.urls import path
from . import views


urlpatterns=[
    path("conference/", views.ConferenceListView.as_view()),
    path("conference/<slug:url>/", views.ConferenceDetailView.as_view()),
    path("register/", views.RegisterCreateView.as_view()),
    path("work/", views.WorkCreateView.as_view()),
]