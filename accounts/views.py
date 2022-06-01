from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Account
from .serializers import AccountSerializer, AccountRegisterSerializer


class AccountModelViewset(ModelViewSet):
    """
    TODO: Create, upadte, put, pacth, Delete
    A viewset for viewing and editing user instances.
    """
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [IsAdminUser]
    # def get_permissions(self):
    #   """Set custom permissions for each action."""
    #   if self.action in ['update', 'partial_update', 'destroy', 'list']:
    #       self.permission_classes = [IsAdminUser, ]
    #   elif self.action in ['create']:
    #       self.permission_classes = [AllowAny, ]
    #   return super().get_permissions()
    # print(self.action)

    # def get_permissions(self):
    #     print(self.action)
    #     try:
    #         # return permission_classes depending on `action` 
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except TypeError: 
    #         # action is not set return default permission_classes
    #         return [permission() for permission in self.permission_classes]


class AccountRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer
