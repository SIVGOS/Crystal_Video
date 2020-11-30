from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.ChunkedUploadDemo.as_view(), name='chunked_upload'),
    path('api/chunked_upload_complete/', views.MyChunkedUploadCompleteView.as_view(), name='api_chunked_upload_complete'),
    path('api/chunked_upload/', views.MyChunkedUploadView.as_view(), name='api_chunked_upload'),
]