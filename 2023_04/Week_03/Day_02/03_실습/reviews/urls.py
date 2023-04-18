from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from reviews.views import like_comment

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('<int:review_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/',
         views.comment_delete, name='comment_delete'),
    path('<int:review_pk>/likes/', views.likes, name='likes'),
    path('<int:review_pk>/comments/<int:comment_pk>/likes/',
         like_comment, name='like_comment'),
    path('<int:review_pk>/emotes/<int:emotion>/', views.emotes, name='emotes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
