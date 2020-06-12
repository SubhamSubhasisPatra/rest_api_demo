from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
#  you can read the api if you are nor authenocated


# use viewsets
from rest_framework import viewsets

from api import serializers
from api import models
from api import permission


# Create your views here.

class HelloApi(APIView):
    # Create an object of serializer Class
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        '''

        :param request:
        :param format:
        :return: Response object
        '''

        api_views = [
            'Use http metod (get , post , pust , delete and patch)',
            'is simir to django view',
            'gives you the ',
            'it mapped manually'
        ]

        return Response({
            'message': 'hello',
            'api_views': api_views
        })

    def post(self, request):
        '''Create a hello message with our name'''
        serializer_post = self.serializer_class(data=request.data)

        if serializer_post.is_valid():
            name = serializer_post.validated_data.get('name')
            message = f'Hey {name}'
            return Response({'message': message})

        else:
            ''':return the a dictonary which contain  all the error generated '''
            return Response(
                serializer_post.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Handel updating object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Update partially '''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'detele'})


class HelloViewSet(viewsets.ViewSet):
    ''' Create a hello api ViewSet '''

    serialiser_class = serializers.HelloSerializer

    def list(self, request):
        ''':return a list of data'''
        viewset_list = [
            'simple',
            'subham', 'subhasis'
        ]
        return Response({'message': 'hello', 'viewset_list': viewset_list})

    def create(self, request):
        '''Create a new hello messae'''
        serialiser_create = self.serialiser_class(data=request.data)
        if serialiser_create.is_valid():
            name = serialiser_create.validated_data.get('name')
            message = f"hey {name} , wecome to viewset"
            return Response({'message': message})
        return Response(serialiser_create.errors
                        , status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        ''' handel getting an object by id'''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        ''' handel updating an object by id'''
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        ''' handel partial update an object by id'''
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        ''' delete an object by id'''
        return Response({'http_method': 'DETELE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permission.UpdateOwnProfile]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    '''Handle create user auth token'''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


...


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = [
        permission.UpdateOwnStatus,
        IsAuthenticated
    ]

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
