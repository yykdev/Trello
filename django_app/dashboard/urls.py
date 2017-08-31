from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^t/$', views.team_dashboard, name='team_dashboard'),
    url(r'^t/create/$', views.team_create_modal, name='team_create_modal'),
    url(r'^b/create/(?P<team_id>\d+)/$', views.board_make, name='board_create_modal'),
    url(r'^c/$', views.card_dashboard, name='card_list'),
]
