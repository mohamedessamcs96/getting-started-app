from django.shortcuts import render
from .models import MenuItem,Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from .serializers import MenuItemSerializer,CategorySerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage
# Create your views here.


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@api_view(['get','post'])
def menu_items(request):
    if(request.method=='GET'):
        items=MenuItem.objects.select_related('category').all()
        category_name=request.query_params.get('category')
        to_price=request.query_params.get('to_price')
        search=request.query_params.get('search')
        ordering=request.query_params.get('ordering')
        perpage=request.query_params.get('perpage',default=2)
        page=request.query_params.get('page',default=1)
        if category_name:
            items=items.filter(category__title=category_name)
        if to_price:
            items=items.filter(price__lte=to_price)
        if search:
            #items=items.filter(search__startswith=search)
            items=items.filter(title__icontains=search)
        if ordering:
            items=items.order_by(ordering)
        paginator=Paginator(items,per_page=perpage)
        try:
            items=paginator.page(number=page)
        except EmptyPage:
            items=[]

        serialized_item=MenuItemSerializer(items,many=True)
        return Response(serialized_item.data)
    elif(request.method=='POST'):
        serialized_item=MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data,status.HTTP_201_CREATED)


# class MenuItemView(generics.ListCreateAPIView):
#     queryset=MenuItem.objects.select_related('category').all()
#     serializer_class=MenuItemSerializer

class CategoryView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer()

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer





@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Some Secret Message"})