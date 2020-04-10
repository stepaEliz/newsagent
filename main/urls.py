from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('main/register/', views.RegisterFormView.as_view(), name='register'),
    path('main/login/', views.LoginFormView.as_view(), name='login'),
    path('main/logout/', views.LogoutView.as_view(), name='logout'),
    path('main/my_news_agent/', views.my_newsagent, name='my_newsagent'),
    path('main/my_news_agent/new_channel', views.new_channel, name='new_channel'),
    path('main/edit_profile', views.edit_profile, name='edit_profile'),
    path('main/my_newsagent_page', views.my_newsagent_page, name='my_newsagent_page'),
    path('main/news_news', views.news_news, name='news_news'),
    path('main/news_politics', views.news_politics, name='news_politics'),
    path('main/tech', views.tech, name='tech'),
    path('main/sports', views.sports, name='sports'),
    path('main/health', views.health, name='health'),
    path('main/fitness', views.fitness, name='fitness'),

]