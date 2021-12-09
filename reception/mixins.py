from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name='dispatch')
class AllowedRolesMixin(LoginRequiredMixin, View):
    allowed_roles = None

    def dispatch(self, *args, **kwargs):
        if not self.request.user.role in self.allowed_roles:
            return redirect(reverse_lazy('error_403'))
        # token = self.request.COOKIES.get('token')
        # if not token:
        #     logout(self.request)
        #     next = self.request.get_full_path()
        #     rev = reverse_lazy('user:login_view')
        #     if next:
        #         url = '{}?next={}'.format(rev, next)
        #         return HttpResponseRedirect(url)
        #     return redirect(rev)
        return super().dispatch(*args, **kwargs)