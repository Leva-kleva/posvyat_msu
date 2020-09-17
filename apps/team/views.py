from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import *
from ..team.forms import TeamForm
#from .models import Team
from .scripts import *


class AllTeamView(View):

    def get(self, request):
        try:
            queryset = Team.objects.order_by("-id")
        except Team.DoesNotExist:
            raise Http404("404")
        return render(request, "team/all_team_view.html", {"teams": queryset})


class TeamView(View):

    def get(self, request, slug_team):
        try:
            queryset = Team.objects.get(id=slug_team)
        except Team.DoesNotExist:
            raise Http404("404")
        return render(request, "team/team_view.html", {"team": queryset})


class AddRegistrationView(View):

    def post(self, request):
        form = request.POST

        a = People.objects.create(
            secondname=form.get('secondname0'),
            firstname=form.get('firstname0'),
            faculty=form.get('faculty0'),
            mail=form.get('mail0'),
            phone=form.get('phone0'),
            vklink=form.get('vk0')
        )
        try:
            w = ""
            for el in dict(form)['where']:
                w += el + ", "
        except:
            w = ""
        #print(dict(form)['where'])

        b = Team.objects.create(
            name=form.get('name'),
            typestudy=form.get('typestudy'),
            cap=a,
            agree=True,
            where=w,
            enter=form.get('enter')
        )

        p1 = People.objects.create(
            secondname=form.get('secondname1'),
            firstname=form.get('firstname1'),
            faculty=form.get('faculty1'),
            mail=form.get('mail1'),
        )

        p2 = People.objects.create(
            secondname=form.get('secondname2'),
            firstname=form.get('firstname2'),
            faculty=form.get('faculty2'),
            mail=form.get('mail2'),
        )

        p3 = People.objects.create(
            secondname=form.get('secondname3'),
            firstname=form.get('firstname3'),
            faculty=form.get('faculty3'),
            mail=form.get('mail3'),
        )

        b.firstman = p1
        b.secondman = p2
        b.thirdman = p3
        b.save()

        if form.get('secondname4'):
            p4 = People.objects.create(
                secondname=form.get('secondname4'),
                firstname=form.get('firstname4'),
                faculty=form.get('faculty4'),
                mail=form.get('mail4'),
            )
            b.fourman = p4

        if form.get('secondname5'):
            p5 = People.objects.create(
                secondname=form.get('secondname5'),
                firstname=form.get('firstname5'),
                faculty=form.get('faculty5'),
                mail=form.get('mail5'),
            )
            b.fiveman = p5

        b.save()

        if form.get('enter') == 'YES':
            return redirect('/success')
        else:
            return redirect('/add')


class RegistrationView(View):

    def get(self, request):
        context = {}
        context['form'] = TeamForm()
        return render(request, "pages/registration.html", context)


class CreateUser(View):

    def get(self, request):
        context = {}
        create_users()
        return render(request, "pages/registration.html", context)
