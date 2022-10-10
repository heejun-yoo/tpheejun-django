from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('billing_auth', views.billing_auth),
  path('window', views.window),
  path('billing_confirm', views.billing_confirm),
  
  path('billing_approve', views.billing_approve),
  path('fail', views.fail),
]