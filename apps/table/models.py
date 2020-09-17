from django.db import models
from ..team.models import Team


class Concurse(models.Model):
    #id
    name = models.CharField("Название", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Конкурс"
        verbose_name_plural = "Конкурсы"


class Ball(models.Model):
    #id
    conc = models.ForeignKey(
        Concurse, verbose_name="Конкурс", on_delete=models.SET_NULL, null=True
        )
    team = models.ForeignKey(
        Team, verbose_name="Команда", on_delete=models.SET_NULL, null=True
        )
    ball = models.IntegerField("балл")
    time = models.IntegerField("Время", default=1)

    def __str__(self):
        return self.conc.name

    class Meta:
        verbose_name = "балл"
        verbose_name_plural = "баллы"
