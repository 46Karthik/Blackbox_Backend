from django.urls import path,re_path
from . import song,fileupload,filestore


urlpatterns = [
    path('', song.storesong, name='login'), 
    # path('profile/', profile.profile, name='profile'),
    # path('profile/<str:username>/', profile.profile, name='profile-detail'),
    # path('login/name/', test.test, name='test'),
    path('songstore/', song.storesong, name='login'),
    #new
    #file upload end point
    path('fileUpload/', fileupload.upload, name='filesupload'),
    #All file 
    path('filestore/', filestore.filestore, name='filestore'),
    path('filestore/<int:id>/', filestore.filestore, name='filestore'),
    
]