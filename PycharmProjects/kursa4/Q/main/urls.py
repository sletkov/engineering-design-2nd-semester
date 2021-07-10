from django.urls import path
from . import views

urlpatterns = [
    path('ask', views.ask, name='ask'),

    #Навигация
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('news', views.news, name='news'),
    path('feedback', views.feedback, name='feedback'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),


    # Страницы разделов
    path('coding',views.coding, name='coding'),
    path('databases', views.databases, name='databases'),
    path('crypto', views.crypto, name='crypto'),
    path('other', views.other, name='other'),



]
