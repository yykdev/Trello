from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^t/$', views.team_dashboard, name='team_dashboard'),
    url(r'^t/create/$', views.team_create_modal, name='team_create_modal'),
    url(r'^t/modify/(?P<team_id>\d+)/$', views.team_modify_modal, name='team_modify_modal'),

    url(r'^b/create/(?P<team_id>\d+)/$', views.board_make, name='board_create_modal'),

    url(r'^c/(?P<board_id>\d+)/$', views.card_dashboard, name='card_list'),
    url(r'^cl/create/(?P<board_id>\d+)/$', views.card_list_make, name='card_list_make'),
    url(r'^c/move/(?P<board_id>\d+)/$', views.update_card_position, name='card_move'),
    url(r'^c/create/(?P<cardlist_id>\d+)/$', views.card_make, name='card_make'),
    url(r'c/detail/(?P<card_id>\d+)/$', views.card_detail, name='card_detail'),
]
