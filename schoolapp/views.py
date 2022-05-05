from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import *
from .utils import *
from .models import *
from .forms import *


class ShowProfile(DataMixin, DetailView):
    model = Students
    template_name = 'schoolapp/index.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'student'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_current_school'] = self.get_school_name(self.request.user.pk)
        context['get_current_class'] = self.get_current_class(self.request.user.pk)
        c_def = self.get_user_context(title='Profile - MySchool')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'schoolapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login - MySchool')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'user_id': self.request.user.pk})
