from django.conf.urls import url
from .views import *


urlpatterns = [

    url(r'^$', index, name='index'),

    url(r'^display_notebook$', display_notebook, name ='display_notebook'),
    url(r'^display_computador$', display_computador, name ='display_computador'),
    url(r'^display_celular$', display_celular, name ='display_celular'),

    url(r'^add_notebook$', add_notebook, name='add_notebook'),
    url(r'^add_computador$', add_computador, name='add_computador'),
    url(r'^add_celular$', add_celular, name='add_celular'),

    url(r'^edit_notebook/(?P<pk>\d+)$', edit_notebook, name='edit_notebook'),
    url(r'^edit_computador(?P<pk>\d+)$', edit_computador, name='edit_computador'),
    url(r'^edit_celular(?P<pk>\d+)$', edit_celular, name='edit_celular'),

    url(r'^delete_notebook/(?P<pk>\d+)$', delete_notebook, name='delete_notebook'),
    url(r'^delete_computador(?P<pk>\d+)$', delete_computador, name='delete_computador'),
    url(r'^delete_celular(?P<pk>\d+)$', delete_celular, name='delete_celular'),

]