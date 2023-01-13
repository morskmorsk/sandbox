# from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


# home view
class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context
