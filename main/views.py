from .models import Type, Food, Comment
from rest_framework.viewsets import ModelViewSet
from .serializers import (TypeSerializer, FoodSerializer, CommentSerializer)

from .permissions import CustomPermission


class TypeView(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [CustomPermission]


class FoodView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [CustomPermission]


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]


