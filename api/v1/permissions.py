from rest_framework.permissions import BasePermission, SAFE_METHODS

from user.models import (
    USER,
    CHECKER,
    APP_CREATOR, REGIONAL_CONTROLLER, MODERATOR, STATE_CONTROLLER, ADMINISTRATOR
)


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != USER:
            return False
        return request.user.is_active


class CheckerPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != CHECKER:
            return False
        return request.user.is_active


class AppCreatorPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != APP_CREATOR:
            return False
        return request.user.is_active


class RegionalControllerPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != REGIONAL_CONTROLLER:
            return False
        return request.user.is_active

class ModeratorPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != MODERATOR:
            return False
        return request.user.is_active


class StateControllerPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != STATE_CONTROLLER:
            return False
        return request.user.is_active

class AdministratorPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role != ADMINISTRATOR:
            return False
        return request.user.is_active