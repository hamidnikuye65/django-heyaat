from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'

class BlogPageView(TemplateView):
    template_name = 'blog.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class PortfolioPageView(TemplateView):
    template_name = 'portfolio.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class TeamPageView(TemplateView):
    template_name = 'team.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'