from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category,Product,File
from .serializers import CategorySerializer,ProductSerializer,FileSerializer


class ProductListView(APIView):

    def get(self,request):

        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True, context = {'request':request})
        return Response(serializer.data)
    
class ProductdetailView(APIView):

    def get(self,request,pk):

        try :
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product,context={'request':request})
        return Response(serializer.data)
    
class CategoryListView(APIView):

    def get (self,request):

        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True, context = {'request':request})
        return Response(serializer.data)
    
class CategorydetailView(APIView):

    def get (self,request,pk):

        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(Category,context={'request':request})
        return Response(serializer.data)
    
class FileListView(APIView):

    def get(self,request,product_id):

        file = File.objects.filter(product_id = product_id)
        serializer = FileSerializer(file,many=True, context={'request':request})
        return Response(serializer.data)

class FiledetailView(APIView):

    def get (self,request,product_id,pk):
        
        try:
            f = File.objects.get(pk=pk,product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(f,context={'request':request})
        return Response(serializer.data)
    