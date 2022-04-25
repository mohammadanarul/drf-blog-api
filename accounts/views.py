from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer, AccountRegisterSerializer


class AccountModelViewset(ModelViewSet):
    """
    TODO: Create, upadte, put, pacth, Delete
    A viewset for viewing and editing user instances.
    """
    # lookup_field = 'id'
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer
