from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^get_book/$', views.get_book, name='get_book'),
    url(r'^update_book/$', views.update_book, name='update_book'),
    url(r'^delete_book/$', views.delete_book, name='delete_book'),
    url(r'^add_library_card/$', views.add_library_card, name='add_library_card'),
    url(r'^get_library_card/$', views.get_library_card, name='get_library_card'),
    url(r'^update_library_card/$', views.update_library_card, name='update_library_card'),
    url(r'^delete_library_card/$', views.delete_library_card, name='delete_library_card'),
    url(r'^check_out_book/$', views.check_out_book, name='check_out_book'),
    url(r'^check_in_book/$', views.check_in_book, name='check_in_book'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^Jon_Library_Logo/$', views.jon_library_logo, name='jon_library_logo'),
    url(r'^get_book_result_main_content/$', views.get_result_main_content, name='main_content'),
    url(r'^bootstrap_example/$', views.bootstrap_example, name='bootstrap_example'),
    #url(r'^get_book/?(?P<b>\d+)?/?$', views.get_book_result, name='get_book_result'),

]