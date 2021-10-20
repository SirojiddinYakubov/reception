from django.http import Http404
from django.shortcuts import redirect


class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object()

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404
        return super().dispatch(request, *args, **kwargs)


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(obj, *args, **kwargs):
            group = None

            # if obj.request.user.role == DIRECTOR:
            #     print(dir(obj))
            # if obj.request.user.groups.exists():
            #     group = obj.request.user.groups.all()[0].name
            try:
                if obj.request.user.role in allowed_roles:
                    return view_func(obj, *args, **kwargs)
                else:
                    return redirect('error_403')
            except:
                return redirect('error_403')

        return wrapper_func

    return decorator