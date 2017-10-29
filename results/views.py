from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Result
from .serializers import ResultSerializer


class ResultList(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDetail(RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
