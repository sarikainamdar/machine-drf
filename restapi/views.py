from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer, PostModelSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


# Create your views here.

def view1(request):
    return render(request, 'view1.html')


@api_view(['GET', 'POST', 'PUT'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def first_api(request):
    if request.method == 'GET':
        name = request.data.get('name')

        city = request.data.get('city')
        return Response({"name": name, "city": city})
    elif request.method == 'POST':
        print(request.data)
        name = request.data.get('name')
        city = request.data.get('city')
        return Response({"name": name, "city": city})
    elif request.method == 'PUT':
        print(request.data)
        name = request.data.get('name')
        city = request.data.get('city')
        return Response({"name": name, "city": city})

class FirstApi(APIView):
    def delete(self, request):
        return Response({"message": "this is delete request"})

    def get(self, request):
        cid = request.query_params.get('id')
        name = request.query_params.get('name')
        print(cid, name)
        return Response({"message": "this is get request"})

    def post(self, request):
        return Response({"message": "this is post request"})

    def put(self, request):
        return Response({"message": "this is put request"})

    def patch(self, request):
        return Response({"message": "this is patch request"})

class PostApi(APIView):
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                post = Post.objects.get(pk=kwargs.get('pk'))
                serializer = PostSerializer(post) # to serialize single instance of model class
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"message": "No Record Found"}, status=status.HTTP_404_NOT_FOUND)
        postdata = Post.objects.all()
        #type(postdata)
        serializer = PostSerializer(postdata, many=True) # to serialize queryset of model class
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            obj = Post.objects.get(pk=kwargs.get('pk'))
            serializer = PostSerializer(data=request.data, instance=obj)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            obj = Post.objects.get(pk=kwargs.get('pk'))
            obj.delete()
            return Response({"message", "No Content Found"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

class PostGenericApi(ListAPIView, CreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

class PostGenRUDAPI(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

class PostViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        post_data = Post.objects.all()
        serializer = PostModelSerializer(post_data, many=True)  # to serialize queryset of model class
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        if pk:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostModelSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"messages": "NO Matching Record Found"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"messages": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk=None):
        if pk:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostModelSerializer(data=request.data, instance=post)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"messages": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"messages": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request, pk=None):
        if pk:
            try:
                post = Post.objects.get(pk=pk)
                post.delete()
                return Response({"messages": "No Content"}, status=status.HTTP_200_OK)
            except:
                return Response({"messages": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"messages": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer





