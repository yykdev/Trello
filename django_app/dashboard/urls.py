from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^t/$', views.team_dashboard, name='team_dashboard'),
    url(r'^c/$', views.card_dashboard, name='card_list'),
]
