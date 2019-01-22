from django.conf.urls import url
from firest_djangoframework.Novi_app import views as nakit_views

urlpatterns = [
    url(r'^list-nakit/$', nakit_views.NakitListView.as_view()),
    url(r'^list-festival/$', nakit_views.FestivalListView.as_view()),
    url(r'^list-stand/$', nakit_views.StandListView.as_view()),
    url(r'^(?P<nakit_id>[\d\w-]+)/nakit/$', nakit_views.NakitRetrieveView.as_view()),
    url(r'^nakit/add/$', nakit_views.NakitCreateView.as_view()),
    url(r'^item/add/$', nakit_views.ItemCreateView.as_view()),
    url(r'^festival/add/$', nakit_views.FestivalCreateView.as_view()),
    url(r'^stand/add/$', nakit_views.StandCreateView.as_view()),
    url(r'^storage/add/$', nakit_views.StorageCreateView.as_view()),
    url(r'^item-viewset/(?P<id>[\d\w-]+)/$', nakit_views.ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    url(r'^(?P<id>[\d\w-]+)/festival/$', nakit_views.FestivalRetrieveView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/festival/edit/$', nakit_views.FestivalUpdateView.as_view()),
    url(r'^(?P<stand_id>[\d\w-]+)/stand/$', nakit_views.StandRetrieveView.as_view()),
    url(r'^(?P<stand_id>[\d\w-]+)/stand/edit/$', nakit_views.StandUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/storage/$', nakit_views.StorageRetrieveView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/storage/edit/$', nakit_views.StoregeUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/nakit/edit/$', nakit_views.NakitUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/item/edit/$', nakit_views.ItemUpdateView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/nakit/delete/$', nakit_views.NakitDestroyView.as_view()),
    url(r'^(?P<id>[\d\w-]+)/festival/delete/$', nakit_views.FestivalDestroyView.as_view()),
    url(r'^(?P<stand_id>[\d\w-]+)/stand/delete/$', nakit_views.StandDestroyView.as_view()),
    url(r'^list-storage/$', nakit_views.StorageListView.as_view()),
]