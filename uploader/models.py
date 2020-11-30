from django.db import models
from chunked_upload.models import ChunkedUpload
# Create your models here.
MyChunkedUpload = ChunkedUpload

class Videos(models.Model):
    video_file = models.FileField(upload_to='post_videos')

