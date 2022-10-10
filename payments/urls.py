from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('window', views.window),
  path('vaapi', views.vaapi),
  path('easypay', views.easypay),
  path('direct', views.direct),
  path('keyinapi', views.keyinapi),
  path('inquiryapi', views.inquiryapi),
  path('cancelapi', views.cancelapi),


  path('success', views.success),
  path('fail', views.fail),

]