from django.urls import path
from .views import DetailViewSet, FolderCreateSet, signup_view, login_view, FolderView


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('create_details/', DetailViewSet.as_view(), name='detail-creater'),
    path('create_folders/', FolderCreateSet.as_view(), name='folder-creater'),
    path('folders/', FolderView.as_view(), name='folder-list'),
    # path('folder/{folder_id}/details')
    # path('user/<int:user_id>/', UserDetail.as_view(), name='user-detail'),
    # path('users/', UserList.as_view(), name='user-list'),
    # path('delete/<int:user_id>/', UserDelete.as_view(), name='user-delete'),
    # path('delete-all/', UserDeleteAll.as_view(), name='user-delete-all'),
]
