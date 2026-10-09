from django.shortcuts import render
from .models import User,Product,Category,Review
from .serializers import UserSerializer,ProductSerializer,CategorySerializer,ReviewSerilaizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .pagination import *
from .filters import *

@api_view(['GET','POST'])
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products = price_filter(products,request.GET)
        products = search(products,request.GET)
        paginator = ProductPagination()
        paginated_products = paginator.paginate_queryset(products,request)
        serializer = ProductSerializer(paginated_products,many=True)
        return paginator.get_paginated_response(serializer.data)


    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)



@api_view(['GET','POST'])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer =CategorySerializer(category,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)




@api_view(['GET','POST'])
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)





@api_view(['GET','POST'])
def review(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerilaizer(review,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReviewSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)




@api_view(['PUT','GET','DELETE'])
def product_det(request,id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({'error':"Not found"},status=404)
    if request.method=="GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method=="PUT":
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    if request.method == "DELETE":
        product.delete()
        return Response(status=204)