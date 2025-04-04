from django.urls import path
from .views import DetailViewSet, FolderCreateSet, FolderList, FolderGetById, FolderGetByTag, IMGCreate, IMGGetById, HotPointCreate, HotPointOnIMGList, TestDataCreate, FolderGetByVIN


urlpatterns = [
     # Details
     path('create_details/', DetailViewSet.as_view(), name='detail-creater'),
     # Folders
     path('create_folders/', FolderCreateSet.as_view(), name='folder-creater'),
     path('folders/', FolderList.as_view(), name='folder-list'),
     path('folder/<int:pk>/',
          view=FolderGetById.as_view(), name='get-folder-on-id'),
     path('folder/tag/<str:folder_tag>/',
          view=FolderGetByTag.as_view(), name='get-folder-on-tag'),
     path('folder/VIN/<str:vin>/',
          view=FolderGetByVIN.as_view(), name='get-folder-on-vin'),
     # IMG
     path('create_IMG/', IMGCreate.as_view(), name='img-creater'),
     path('IMG/<int:img_id>/',
          view=IMGGetById.as_view(), name='get-img-on-id'),
     # Hot points
     path('create_hpoint/', HotPointCreate.as_view(), name='h_point-creater'),
     path('hpoints/<int:img_id>/',
          view=HotPointOnIMGList.as_view(), name='get-h_point-by-img'),
     # Test data
     path('test_data/create/<str:type_of_data>/',
          TestDataCreate.as_view(), name='test-data-creater'),
]
