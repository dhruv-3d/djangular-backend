from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class ContactListAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    #permission_classes = (IsAdminUser,)

    # @action(methods=['get'], detail=False)
    # def fetchContact(self, request):
    #     acon = self.get_queryset()
    #     serializer = self.get_serializer_class()(acon)
    #     print(serializer.data)
    #     return Response(serializer.data[0]['first_name'])
