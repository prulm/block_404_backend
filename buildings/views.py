from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import *

class BuildingCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    
    def post(self, *args, **kwargs):
        if(self.request.data.get('building')):
            serializer = BuildingSerializer(data=self.request.data.get('building'))
            if (serializer.is_valid()):
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if (self.request.data.get('attachments')):
            serializer = AttachmentsSerializer(data=self.request.data.get('attachments'))
            if (serializer.is_valid()):
                serializer.save(building=Building.objects.last())
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        if (self.request.data.get('pictures')):
            serializer = PicturesSerializer(data=self.request.data.get('pictures'))
            if (serializer.is_valid()):
                serializer.save(building=Building.objects.last())
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Successful", status=status.HTTP_201_CREATED)