
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views

from classes2 import views as api_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),




    path('classrooms/list/', api_views.ClassroomList.as_view(), name="classroom-list"), 
    path('classrooms/detail/<int:classroom_id>/', api_views.ClassroomDetails.as_view(), name="classroom-details"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/<int:classroom_id>/update/', api_views.ClassroomUpdate.as_view(), name='classroom-update'),
    path('api/<int:classroom_id>/delete/', api_views.ClassroomDelete.as_view(), name='classroom-delete'),
    path('api/create/', api_views.ClassroomCreate.as_view(), name='classroom-create'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
