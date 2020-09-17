from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Page
from django.shortcuts import render
from django.http import Http404
from ..team.forms import TeamForm

class PageView(View):

    def get(self, request, slug="/"):
        if slug == "/" or slug == "":
            slug = "base"
            return render(request, "pages/"+slug+".html")
        else:
            try:
                page = Page.objects.get(url=slug, draft=False)
            except Page.DoesNotExist:
                raise Http404("404")
            if slug == "success" or slug == "add":
                context = {}
                context['form'] = TeamForm()
                return render(request, "pages/"+slug+".html", context)
            return render(request, "pages/"+slug+".html", {"page": page})
