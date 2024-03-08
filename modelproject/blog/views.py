from django.shortcuts import render

from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

'''
전체 블로그를 조회
'''
@api_view(['GET']) # GET 요청만 받겠다.
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

'''
한 블로그 조회
'''
@api_view(['GET'])
def blog_detail(request, pk):
    try: # 아래 코드를 시도
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Blog.DoesNotExist: # 예외(오류) 발생 시 아래 코드 실행
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = BlogSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = BlogSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)