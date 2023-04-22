from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('categoria/<str:categoria>',
         views.PostCategoria.as_view(),
         name='post_categoria'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
]
