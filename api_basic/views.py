import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from rest_framework.fields import REGEX_TYPE
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .models import PastEvent, PostImage, TeamMember, Department,UpcomingEvent
# , Pdf, Article ,Video
from .serializers import PastEventSerializer, PostImageSerializer, TeamMemberSerializer, DepartmentSerializer,UpcomingEventSerializer
# , PdfSerializer,ArticleSerializer, UserSerializer,VideoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import mixins
from .models import PostImage, PastEvent
from datetime import datetime
# Create your views here.



class DepartmentView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


    def get(self,request):
        return self.list(request)
    
    # def post(self,request):
    #     return self.create(request)

class TeamMemberView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()


    def get(self,request):
        return self.list(request)

class UpcomingEventView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = UpcomingEventSerializer
    queryset = UpcomingEvent.objects.all().filter(date__gte=datetime.today()).order_by('date')
    # ordering_fields='__all__' 

    def get(self,request):
        return self.list(request)

class PastEventViewSet(viewsets.ModelViewSet):
    queryset = PastEvent.objects.all()
    serializer_class = PastEventSerializer

class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
   
# class PastEventView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     serializer_class = PostImageSerializer
#     queryset = PastEvent.objects.all()


#     def get(self,request):
#         return self.list(request)


    # def post(self,request):
    #     return self.create(request)
    
    



# class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,
# mixins.RetrieveModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

#     lookup_field = 'id'

#     def get(self,request,id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
    
#     # def post(self,request):
#     #     return self.create(request)
    
#     def put(self,request,id=None):
#         return self.update(request,id)
    
#     def delete(self,request):
#         return self.destroy(request,id)

# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','POST'])
# def video_list(request):
#     if request.method == 'GET':
#         articles = Video.objects.all()
#         serializer = VideoSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = VideoSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','POST'])
# def pdf_list(request):
#     if request.method == 'GET':
#         articles = Pdf.objects.all()
#         serializer = PdfSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PdfSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def auth_user(request):
#     if request.method == 'POST':
#         userData = request.data
#         try:
#             user = authenticate(username=userData['username'], password=userData['password'])
#             if user is not None:
#                 return Response(True,status=status.HTTP_200_OK)
#             else:
#                 return Response(False,status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response(False,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
# def user_list(request):
#     if request.method == 'GET':
#         u = User.objects.all()
#         serializer = UserSerializer(u,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         userData = request.data
#         try:
#             User.objects.create_user(userData['username'], userData['email'], userData['password'])
#             return Response("Created",status=status.HTTP_201_CREATED)
#         except:
#             return Response("Failed",status=status.HTTP_400_BAD_REQUEST)

#         # serializer = PdfSerializer(data=request.data)

#         # if serializer.is_valid():
#         #     serializer.save()
#         # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
    
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data) 
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class ArticleDetails(APIView):

#     def get_object(self,id):
#         try:
#             return Article.objects.get(id=id)
    
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self,request,id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data) 
    
#     def put(self,request,id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
#     def delete(self,request,id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)