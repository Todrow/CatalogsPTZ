from django.urls import path
from .views import DetailViewSet, FolderCreateSet, FolderList, FolderGetById, IMGCreate, IMGGetById, HotPointCreate, HotPointOnIMGList


urlpatterns = [
    # Sing up/in
#     path('signup/', signup_view, name='signup'),
#     path('login/', login_view, name='login'),
    # Details
    path('create_details/', DetailViewSet.as_view(), name='detail-creater'),
    # Folders
    path('create_folders/', FolderCreateSet.as_view(), name='folder-creater'),
    path('folders/', FolderList.as_view(), name='folder-list'),
    path('folder/<int:folder_id>/',
         view=FolderGetById.as_view(), name='get-folder-on-id'),
    # IMG
    path('create_IMG/', IMGCreate.as_view(), name='img-creater'),
    path('IMG/<int:img_id>/',
         view=IMGGetById.as_view(), name='get-img-on-id'),
    # Hot points
    path('create_hpoint/', HotPointCreate.as_view(), name='h_point-creater'),
    path('hpoints/<int:img_id>/',
         view=HotPointOnIMGList.as_view(), name='get-h_point-by-img'),
]
