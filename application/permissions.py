from django.http import Http404


class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object()

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404
        return super().dispatch(request, *args, **kwargs)