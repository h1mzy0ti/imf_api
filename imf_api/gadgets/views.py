import random
import uuid
from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Gadget
from .serializers import GadgetSerializer, GadgetCreateSerializer


class GadgetListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gadgets = Gadget.objects.filter(owner=request.user)
        serialized_data = []
        for gadget in gadgets:
            data = GadgetSerializer(gadget).data
            data["success_probability"] = f"{random.randint(50, 100)}%"
            serialized_data.append(data)
        return Response(serialized_data)

    def post(self, request):
        serializer = GadgetCreateSerializer(data=request.data)
        if serializer.is_valid():
            gadget = serializer.save(owner=request.user)
            return Response(GadgetSerializer(gadget).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GadgetUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            gadget = Gadget.objects.get(pk=pk, owner=request.user)
        except Gadget.DoesNotExist:
            return Response({"detail": "Gadget not found."}, status=status.HTTP_404_NOT_FOUND)

        gadget.name = request.data.get('name', gadget.name)
        gadget.status = request.data.get('status', gadget.status)
        gadget.save()
        return Response(GadgetSerializer(gadget).data)


class GadgetDecommissionView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            gadget = Gadget.objects.get(pk=pk, owner=request.user)
        except Gadget.DoesNotExist:
            return Response({"detail": "Gadget not found."}, status=status.HTTP_404_NOT_FOUND)

        gadget.status = 'Decommissioned'
        if hasattr(gadget, 'decommissioned_at'):
            gadget.decommissioned_at = datetime.now()
        gadget.save()
        return Response(GadgetSerializer(gadget).data)


class GadgetSelfDestructView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            gadget = Gadget.objects.get(pk=pk, owner=request.user)
        except Gadget.DoesNotExist:
            return Response({"detail": "Gadget not found."}, status=status.HTTP_404_NOT_FOUND)

        confirmation_code = str(uuid.uuid4())
        return Response({
            "gadget_id": str(gadget.id),
            "message": f"Self-destruct sequence initiated for {gadget.name}.",
            "confirmation_code": confirmation_code
        }, status=status.HTTP_200_OK)
    

class GadgetsStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        status_param = request.query_params.get('status')
        if not status_param:
            return Response({"detail": "Status query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        gadgets = Gadget.objects.filter(pk=pk, status=status_param, owner=request.user)
        
        if not gadgets.exists():
            return Response({"detail": "Gadget not found."}, status=status.HTTP_404_NOT_FOUND)

        serialized = GadgetSerializer(gadgets, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)