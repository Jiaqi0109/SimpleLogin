from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/', views.to_sign_up, name='to_sign_up'),
    url(r'^lkajsldfkj/', views.sign_up, name='sign_up'),
    url(r'^xicjvijwiw/', views.sign_in, name='sign_in'),
]