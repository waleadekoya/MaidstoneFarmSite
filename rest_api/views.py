# from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer

from .serializers import PenSerializer, SnailsActivitySerializer, SnailsInventorySerializer, \
    EggsInventorySerializer, StocksTransferSerializer
from .models import Pen, SnailsActivity, SnailsInventory, EggsInventory, StocksTransfer


# Create your views here.


class PenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pen numbers to be viewed or edited
    """
    queryset = Pen.objects.all().order_by('number')
    serializer_class = PenSerializer


class EggsInventoryViewSet(viewsets.ModelViewSet):
    max_id = EggsInventory.objects.latest('id').id
    queryset = EggsInventory.objects.order_by('-dateTimeRecorded')  # .filter(id=max_id)
    serializer_class = EggsInventorySerializer


class SnailsActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snails activity to be viewed or edited
    https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
    """
    queryset = SnailsActivity.objects.all().order_by('-dateTimeRecorded')
    serializer_class = SnailsActivitySerializer
    # renderer_classes = [BrowsableAPIRenderer]


class SnailsCurrentInventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snails total inventory as at particular date to be viewed or edited
    https://www.django-rest-framework.org/tutorial/quickstart/
    """
    queryset = SnailsInventory.objects.all().order_by('dateTimeRecorded')
    serializer_class = SnailsInventorySerializer
    permission_classes = [permissions.IsAuthenticated]


class StocksTransferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pen numbers to be viewed or edited
    """
    queryset = StocksTransfer.objects.all().order_by('dateTimeRecorded')
    serializer_class = StocksTransferSerializer
