from django.urls import path, include
from .views import view1, first_api, FirstApi, PostApi, PostGenericApi, PostGenRUDAPI, PostViewSet, PostModelViewSet
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
router = routers.SimpleRouter()
router.register("postviewset", PostViewSet, basename='postviewset')
router1 = routers.DefaultRouter()
router1.register('postmodelviewset', PostModelViewSet)
urlpatterns = [
    path('view1/', view1, name='view1'),
    path('firstapi/', first_api, name='first_api'),
    path('capi/', FirstApi.as_view(), name='capi'),
    path('post/', PostApi.as_view(), name='post'),
    path('post/<int:pk>/', PostApi.as_view(), name='post-obj'),
    path('postgen/', PostGenericApi.as_view(), name='post-gen-api'),
    path('postgen/<int:pk>/', PostGenRUDAPI.as_view(), name='post-gen-api'),
    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('access/', ObtainAuthToken.as_view(), name='access-token')
]