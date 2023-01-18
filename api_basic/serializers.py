from django.db import models
from django.db.models import fields
from rest_framework import serializers
# , Pdf,Article, Video
# from django.contrib.auth.models import User
from .models import PastEvent, PostImage, TeamMember, Department, UpcomingEvent

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    members = TeamMemberSerializer(many=True,read_only=True)
    class Meta:
        model = Department
        fields = '__all__'

class UpcomingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingEvent
        fields = '__all__'

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class PastEventSerializer(serializers.ModelSerializer):
    post = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = PastEvent
        fields = '__all__'

# class PastEventSerializer(serializers.ModelSerializer):
#     #   tp=serializers.StringRelatedField(many=True, read_only=True)
#       class Meta:
#         model = PastEvent
#         fields = '__all__'
        
# # your image serializer
# class PostImageSerializer(serializers.ModelSerializer):
#   tp = PastEventSerializer(many=True,read_only=True)
#   class Meta:
#     model = PostImage
#     fields = '__all__'
     # posts is a related_name given while defining foreign key

# class PastEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PastEvent
#         fields = '__all__'

# class PostImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=PostImage
#         fields = '__all__'

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ['name','url']

# class PdfSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pdf
#         fields = ['name','url']


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ['id','username','password','email']

