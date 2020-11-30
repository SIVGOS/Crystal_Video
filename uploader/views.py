from django.views.generic.base import TemplateView
from chunked_upload.views import ChunkedUploadView, ChunkedUploadCompleteView
from django.shortcuts import render
from django.http import HttpResponse
from .models import MyChunkedUpload, Videos

class ChunkedUploadDemo(TemplateView):
    template_name = 'chunked_upload_demo.html'


class MyChunkedUploadView(ChunkedUploadView):

    model = MyChunkedUpload
    field_name = 'the_file'

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass


class MyChunkedUploadCompleteView(ChunkedUploadCompleteView):

    model = MyChunkedUpload

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass

    def on_completion(self, uploaded_file, request):
        # Do something with the uploaded file.
        vid = Videos.objects.create(video_file=uploaded_file)
        vid.save()


    def get_response_data(self, chunked_upload, request):
        return {'message': ("You successfully uploaded '%s' (%s bytes)!" %
                            (chunked_upload.filename, chunked_upload.offset))}  
                            
                              
