from django.urls import path
from . import views
urlpatterns = [
    path('',views.anasayfa_view, name="home"),
    path('video',views.video, name="video"),
    path('hakkında',views.hakkinda, name="hakkında"),
    path('comment',views.comment_detail, name="comment"),
    path('video/<slug:videoId>',views.video_details, name="video_detail"),
    path('video/<slug:videoId>/delete',views.deletevideo_confirm, name="delete_video_confirm"),
    path('video/<slug:videoId>/delete_video',views.deletevideo, name="delete_video"),
    path('comment/<slug:videoId>/<slug:commentId>',views.comment_detail_2,name="comment_detail")
    
]