from django.conf.urls import url
from firest_djangoframework.Novi_app import views as nakit_views

urlpatterns = [
    url(r'^list-nakit/$', nakit_views.NakitListView.as_view()),
    url(r'^(?P<nakit_id>[\d\w-]+)/nakit/$', nakit_views.NakitRetrieveView.as_view()),
    url(r'^nakit/add/$', nakit_views.NakitCreateView.as_view()),
    url(r'^item/add/$', nakit_views.ItemCreateView.as_view()),
    url(r'^storage/add/$', nakit_views.StorageCreateView.as_view()),
    url(r'^(?P<item_id>[\d\w-]+)/storage/$', nakit_views.StorageRetrieveView.as_view()),
    url(r'^(?P<item_id>[\d\w-]+)/storage/edit/$', nakit_views.StoregeUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/nakit/edit/$', nakit_views.NakitUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/item/edit/$', nakit_views.ItemUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/nakit/delete/$', nakit_views.NakitDestroyView.as_view()),
    url(r'^list-storage/$', nakit_views.StorageListView.as_view()),
]