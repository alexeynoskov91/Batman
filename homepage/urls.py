from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homepage),
    path('', views.Home.as_view(), name='homepage'),
    path('articles/<int:pk>', views.ArticlesDetailView.as_view(), name='article_page'),
    path('edit_page', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update_page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete_page/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_page'),
]