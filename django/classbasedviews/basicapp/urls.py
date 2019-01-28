from django.urls import path, include
from . import views


app_name='basicapp'
urlpatterns = [
	path('',views.SchoolList.as_view(),name='list'),
	path('<int:pk>/',views.SchoolDetail.as_view(),name="detail"),
	path('new/',views.CreateSchool.as_view(),name='create'),
	path('<int:pk>/delete/',views.DeleteSchool.as_view(),name='delete'),
	path('<int:pk>/update/',views.UpdateSchool.as_view(),name='update'),




]
