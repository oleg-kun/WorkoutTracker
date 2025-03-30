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
        if hasattr(obj, "user"):                 #if Workout
            return bool(
                request.user and
                request.user.is_authenticated and obj.user == request.user
            )
        if hasattr(obj.workout_connection, "user"):         #if Exercise
            return bool(
                request.user and
                request.user.is_authenticated and obj.workout_connection.user == request.user
            )

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated
        )
