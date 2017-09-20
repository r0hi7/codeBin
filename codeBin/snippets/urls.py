from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$',views.snippet_list,name='all_snippets'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_details,name='individual_snippet'),
]
