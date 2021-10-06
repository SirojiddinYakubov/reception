from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.authtoken.models import Token

import user.views


@method_decorator(login_required, name='dispatch')
class AllowedRolesMixin(LoginRequiredMixin, View):
    allowed_roles = None

    def dispatch(self, *args, **kwargs):
        if not self.request.user.role in self.allowed_roles:
            raise Http404

        try:
            token = self.request.COOKIES.get('token')
            Token.objects.get(key=token)
        except ObjectDoesNotExist:
            logout(self.request)
            next = self.request.get_full_path()
            rev = reverse_lazy('user:login_view')
            if next:
                url = '{}?next={}'.format(rev, next)
                return HttpResponseRedirect(url)
            return redirect(rev)

        return super().dispatch(*args, **kwargs)