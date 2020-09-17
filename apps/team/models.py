from django.db import models
from django.db.models import Sum
from django.urls import reverse
from datetime import date
from django.core.validators import RegexValidator
#from ..table.models import Ball
from django.contrib.auth.models import User


#class Faculty(models.Model):
#    name = models.CharField("Название", max_length=140)


#class TypeStudy(models.Model):
#    name = models.CharField("Тип", max_length=140)

class People(models.Model):
    FACULTY = (
        ("0", "------"),
        ("1", "Механико–математический факультет"),
        ("2", "Факультет вычислительной математики и кибернетики"),
        ("3", "Физический факультет"),
        ("4", "Химический факультет"),
        ("5", "Факультет наук о материалах"),
        ("6", "Биологический факультет"),
        ("7", "Факультет биоинженерии и биоинформатики"),
        ("8", "Факультет почвоведения"),
        ("9", "Геологический факультет"),
        ("10", "Географический факультет"),
        ("11", "Факультет фундаментальной медицины"),
        ("12", "Факультет фундаментальной физико-химической инженерии"),
        ("13", "Биотехнологический факультет"),
        ("14", "Факультет космических исследований"),
        ("15", "Исторический факультет"),
        ("16", "Филологический факультет"),
        ("17", "Философский факультет"),
        ("18", "Экономический факультет"),
        ("19", "Юридический факультет"),
        ("20", "Факультет журналистики"),
        ("21", "Факультет психологии"),
        ("22", "Институт стран Азии и Африки"),
        ("23", "Социологический факультет"),
        ("24", "Факультет иностранных языков и регионоведения"),
        ("25", "Факультет государственного управления"),
        ("26", "Факультет мировой политики"),
        ("27", "Факультет искусств"),
        ("28", "Факультет глобальных процессов"),
        ("29", "Факультет педагогического образования"),
        ("30", "Факультет политологии"),
        ("31", "Высшая школа бизнеса (факультет)"),
        ("32", "Московская школа экономики(факультет)"),
        ("33", "Высшая школа перевода(факультет)"),
        ("34", "Высшая школа государственного администрирования(факультет)"),
        ("35", "Высшая школа государственного аудита(факультет)"),
        ("36", "Высшая школа управления и инноваций(факультет)"),
        ("37", "Высшая школа инновационного бизнеса(факультет)"),
        ("38", "Высшая школа современных социальных наук(факультет)"),
        ("39", "Высшая школа телевидения(факультет)"),
        ("40", "Высшая школа культурной политики и управления в гуманитарной сфере(факультет)")
        )

    secondname = models.CharField("Фамилия", max_length=100, blank=True)
    firstname = models.CharField("имя", max_length=100, blank=True)
    faculty = models.CharField("факультет", max_length=200, choices=FACULTY, blank=True)
    mail = models.CharField("e-mail", max_length=1000, blank=True)
    #phone_regex = RegexValidator(regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\-]?)?[\d\- ]{7,10}$')
    phone = models.CharField("phone", max_length=20, blank=True)
    vklink = models.CharField("VK", max_length=150, blank=True)

    def __str__(self):
        return self.secondname + " " + self.firstname

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

#class Where(models.Model):
#    text = models.CharField("вариант", max_length=250)


class Team(models.Model):
    TYPESTUDY = (
        ("бак", "бакалавриат"),
        ("спец", "специалитет"),
        ("маг", "магистратура"),
        )
    WHERE = (
        ("Увидел афишу/получил флаер", "Увидел афишу/получил флаер"),
        ("Узнал от друзей", "Узнал от друзей"),
        ("Из группы Профсоюзной организации VK (vk.com/msuprofcom)", "Из группы Профсоюзной организации VK (vk.com/msuprofcom)"),
        ("Из аккаунта Профсоюзной организации в Instagram (instagram.com/msuprofcom)", "Из аккаунта Профсоюзной организации в Instagram (instagram.com/msuprofcom)"),
        ("Прочитал в Профсоюзном путеводителе для студентов МГУ", "Прочитал в Профсоюзном путеводителе для студентов МГУ"),
        ("Узнал на факультете (кураторы/групповоды/...)", "Узнал на факультете (кураторы/групповоды/...)"),
        ("Другое", "Другое"),
        )
    ENTER = (
        ('YES', 'Да'),
        ('NO', 'Нет')
    )

    account = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField("Название", max_length=6000)
    typestudy = models.CharField("форма обучения", max_length=200, choices=TYPESTUDY)

    cap = models.ForeignKey(
        People, verbose_name="капитан", on_delete=models.SET_NULL, null=True, related_name="capitan", blank=True
        )
    firstman = models.ForeignKey(
        People, verbose_name="участник 1", on_delete=models.SET_NULL, null=True, related_name="first"
        )
    secondman = models.ForeignKey(
        People, verbose_name="участник 2", on_delete=models.SET_NULL, null=True, related_name="second"
    )
    thirdman = models.ForeignKey(
        People, verbose_name="участник 3", on_delete=models.SET_NULL, null=True, related_name="third"
    )
    fourman = models.ForeignKey(
        People, verbose_name="участник 4", on_delete=models.SET_NULL, null=True, blank=True, related_name="four"
    )
    fiveman = models.ForeignKey(
        People, verbose_name="участник 5", on_delete=models.SET_NULL, null=True, blank=True, related_name="five"
    )

    agree = models.BooleanField("Согласие", default=False)
    where = models.CharField("где узнал?", max_length=2000)#, choices=WHERE)
    #where = models.MultiSelectField(choices=WHERE, max_lenght=1000, max_choices=7)
    enter = models.CharField("вступил в опк?", max_length=4, choices=ENTER)

    #kek = models.ManyToManyField(Ball, blank=True)
    score = models.IntegerField("Сумма баллов", default=0)


    #score = 0 #Ball.objects.values("team").annotate(s=Sum("ball"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''/posts/<slug:slug_post>/'''
        return reverse("team", kwargs={"slug_team": self.id})

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
