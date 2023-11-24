"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),


    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_state_master_add', views.admin_state_master_add, name='admin_state_master_add'),
    path('admin_state_master_view', views.admin_state_master_view, name='admin_state_master_view'),
    path('admin_state_master_delete', views.admin_state_master_delete, name='admin_state_master_delete'),

    path('admin_district_master_add', views.admin_district_master_add, name='admin_district_master_add'),
    path('admin_district_master_view', views.admin_district_master_view, name='admin_district_master_view'),
    path('admin_district_master_view2', views.admin_district_master_view2, name='admin_district_master_view2'),
    path('admin_district_master_delete', views.admin_district_master_delete, name='admin_district_master_delete'),

    path('admin_place_master_add', views.admin_place_master_add, name='admin_place_master_add'),
    path('admin_place_master_view', views.admin_place_master_view, name='admin_place_master_view'),
    path('admin_place_master_delete', views.admin_place_master_delete, name='admin_place_master_delete'),
    path('admin_place_master_view2', views.admin_place_master_view2, name='admin_place_master_view2'),

    path('admin_crime_type_add', views.admin_crime_type_add, name='admin_crime_type_add'),
    path('admin_crime_type_view', views.admin_crime_type_view, name='admin_crime_type_view'),
    path('admin_crime_type_delete', views.admin_crime_type_delete, name='admin_crime_type_delete'),

    path('admin_station_master_add', views.admin_station_master_add, name='admin_station_master_add'),
    path('admin_station_master_update', views.admin_station_master_update, name='admin_station_master_update'),
    path('admin_station_master_delete', views.admin_station_master_delete, name='admin_station_master_delete'),
    path('admin_station_master_view', views.admin_station_master_view, name='admin_station_master_view'),

    path('admin_station_user_view', views.admin_station_user_view, name='admin_station_user_view'),
    path('admin_station_user_add', views.admin_station_user_add, name='admin_station_user_add'),
    path('admin_station_user_delete', views.admin_station_user_delete, name='admin_station_user_delete'),

    path('station_login', views.station_login, name='station_login'),
    path('station_changepassword', views.station_changepassword, name='station_changepassword'),
    path('station_logout', views.station_logout, name='station_logout'),
    path('station_home', views.station_home, name='station_home'),

    path('station_station_master_view', views.station_station_master_view, name='station_station_master_view'),
    path('station_station_master_view2', views.station_station_master_view2, name='station_station_master_view2'),

    path('station_station_user_view', views.station_station_user_view, name='station_station_user_view'),
    path('station_station_user_view2', views.station_station_user_view2, name='station_station_user_view2'),

    path('station_notice_board_master_add', views.station_notice_board_master_add, name='station_notice_board_master_add'),
    path('station_notice_board_master_view', views.station_notice_board_master_view, name='station_notice_board_master_view'),
    path('station_notice_board_master_delete', views.station_notice_board_master_delete, name='station_notice_board_master_delete'),
    path('station_notice_board_master_view2', views.station_notice_board_master_view2, name='station_notice_board_master_view2'),

    path('station_look_out_master_add', views.station_look_out_master_add, name='station_look_out_master_add'),
    path('station_look_out_master_view', views.station_look_out_master_view, name='station_look_out_master_view'),
    path('station_look_out_master_delete', views.station_look_out_master_delete, name='station_look_out_master_delete'),
    path('station_look_out_master_view2', views.station_look_out_master_view2, name='station_look_out_master_view2'),

    path('station_user_report_master_view', views.station_user_report_master_view, name='station_user_report_master_view'),
    path('station_report_pic_view', views.station_report_pic_view, name='station_report_pic_view'),

    path('station_report_followups_add', views.station_report_followups_add, name='station_report_followups_add'),
    path('station_report_followups_view', views.station_report_followups_view, name='station_report_followups_view'),


    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),

    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_details_update', views.user_details_update, name='user_details_update'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_station_master_view', views.user_station_master_view, name='user_station_master_view'),
    path('user_station_master_search', views.user_station_master_search, name='user_station_master_search'),
    path('user_look_out_master_view', views.user_look_out_master_view, name='user_look_out_master_view'),
    path('user_notice_board_master_view', views.user_notice_board_master_view, name='user_notice_board_master_view'),

    path('user_report_master_add', views.user_report_master_add, name='user_report_master_add'),
    path('user_report_master_view', views.user_report_master_view, name='user_report_master_view'),
    path('user_report_pic_view', views.user_report_pic_view, name='user_report_pic_view'),

    path('user_report_followups_view', views.user_report_followups_view, name='user_report_followups_view'),

]
