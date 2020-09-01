from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="listings"),
    path('search', views.search, name="search"),
    path('single', views.listings, name="singlelist"),
    path('<int:listing_id>', views.booking, name="booking"),
    path('booking/create/', views.BookingCreate.as_view(), name='booking_create'),
    path('booking/<int:pk>/update/', views.BookingUpdate.as_view(), name='booking_update'),
    path('booking/<int:pk>/delete/', views.BookingDelete.as_view(), name='booking_delete'),
    path('booking/<int:pk>/list/', views.BookingList.as_view(), name='booking_list'),
]

