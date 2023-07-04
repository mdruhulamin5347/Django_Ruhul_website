from django.urls import path
from .views import POST,LIST,DETAILS,EDIT,DELETE,SEARCH,FILTER,LIKEPOST,COMMENT,PICADD,NOTIFICATION_R,DELETECOMMENT

urlpatterns = [
    #path('',POST.as_view(),name=''),
    path('',POST,name=''),
    path('list/',LIST.as_view(),name='list'),
    path('details/<int:pk>',DETAILS.as_view(), name='details'),
    path('edit/<int:pk>',EDIT.as_view(), name='edit'),
    path('delete/<int:pk>',DELETE.as_view(),name='delete'),
    path('likepost/<int:id>',LIKEPOST,name='likepost'),
    path('deletecomment/<int:id>',DELETECOMMENT,name='deletecomment'),
    path('notification/',NOTIFICATION_R,name='notification'),
    path('picadd/<int:id>',PICADD,name='picadd'),
    path('search/',SEARCH, name='search'),
    path('filter/',FILTER, name='filter'),
    path('comment/',COMMENT, name='comment'),
]
