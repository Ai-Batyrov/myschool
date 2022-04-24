from django.views import View


class Home(View):
    template_name = 'schoolapp/index.html'
