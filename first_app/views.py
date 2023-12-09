from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated
from .import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .import paginations
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes=[IsAuthenticated]
    permission_classes=[permissions.AdminOrReadOnly]
    # permission_classes=[AdminOrReadOnly]
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'description']
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price']
    # pagination_class=paginations.ProductPagination
    # pagination_class=paginations.LimitOffsetPagination
    pagination_class=paginations.ProductCursorPagination
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.ReviewerOrReadOnly]
    queryset=models.ProductReview.objects.all()
    serializer_class=serializers.ProductReviewSerializer
    # filter_backends = [DjangoFilterBackend]
    # # filterset_fields = ['user__username']
    # filterset_fields = ['rating','product']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']
    
    # filtering against query parameters 
# class ProductReviewViewSet(viewsets.ModelViewSet):
#     permission_classes=[permissions.ReviewerOrReadOnly]
#     # queryset=models.ProductReview.objects.all()
#     serializer_class=serializers.ProductReviewSerializer
    # def get_queryset(self):
    #     queryset=models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username') # username er under e j value ta ache seta automatic chole asbe 
    #     # get function jodi kono ekta value na pai taile none return korbe 
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username) #foreign key er khetre double underscore diye access korte hoi
    #     return queryset
    # __icontains dewa mane case sensitive bepar ta dekhbe na j Karim or karim jekono tai niye nibe