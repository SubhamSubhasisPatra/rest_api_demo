from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit there own profile '''

    def has_object_permission(self, request, view, obj):
        '''
        This function check the user is authenticated or not
        it return either a true or a False value

        '''

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    '''allow to update these own permission'''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
