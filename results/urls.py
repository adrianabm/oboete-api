from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ResultList, ResultDetail

urlpatterns = [
    url(r'^results/$', ResultList.as_view()),
    url(r'^results/(?P<pk>[0-9]+)/$', ResultDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
