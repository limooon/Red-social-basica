from django.urls import path
from .views import HomePageView, SamplePageView,logout_view

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('logout/', logout_view, name='logout'),
]