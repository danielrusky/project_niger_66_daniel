from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from payment.models import Pay
from payment.serializers import PaySerializer
from rest_framework.filters import OrderingFilter


class PayViewSet(viewsets.ModelViewSet):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('is_paid', 'pay_method',)
    ordering_fields = ('payday',)