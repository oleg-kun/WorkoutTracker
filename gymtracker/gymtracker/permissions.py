from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsUserOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return bool(
#             request.method in SAFE_METHODS or
#             request.user and
#             request.user.is_authenticated and obj.user == request.user
#         )


class UserOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):  # if Workout
            if request.user.is_authenticated and obj.user == request.user:
                return True
            raise PermissionDenied("У вас нет доступа к этой тренировке")
        if hasattr(obj.workout_connection, "user"):  # if Exercise
            if request.user.is_authenticated and obj.workout_connection.user == request.user:
                return True
            raise PermissionDenied("У вас нет доступа к этому упражнению")
        raise PermissionDenied("Невозможно проверить права доступа")

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        raise PermissionDenied("Для доступа пользователь должен быть авторизован")
