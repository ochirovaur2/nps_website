from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<int:ticket_id>/<str:user_id>/<str:time>', views.index, name='index'),
    path('response/', views.response, name='response'),
    path('recaptcha_false/', views.recaptcha_false, name='recaptcha_false'),
    path('dubble_comment/', views.dubble_comment, name='dubble_comment'),
]
