from django.urls import path,include
from .views import DepartmentView,PastEventViewSet,TeamMemberView,UpcomingEventView,PostImageViewSet
# , GenericAPIView,  article_list,article_detail, auth_user, pdf_list, video_list,user_list,ArticleDetails
from django.contrib import admin
from api_basic import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post', views. PastEventViewSet, basename='post')
router.register('postimage', views.PostImageViewSet, basename='postimage')

urlpatterns = [
    # path('article/', article_list),
    # path('article/<int:id>/', GenericAPIView.as_view()),
    # path('detail/<int:id>/', ArticleDetails.as_view()),
    # path('video',video_list),
    # path('pdf',pdf_list),
    # path('user',user_list),
    # path('authUser',auth_user),
    path('department/', DepartmentView.as_view()),
    path('memberList/', TeamMemberView.as_view()),
    path('UpcomingEventList/', UpcomingEventView.as_view()),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]