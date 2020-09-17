from django.db import models
from ..team.models import Team


class Product(models.Model):
    #id
    name = models.CharField("Название", max_length=150)
    description = models.CharField("Описание", max_length=150, default="Описание", blank=True)
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField("цена")
    balance = models.IntegerField("Остаток на складе:", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    STATUS = (
        ('Отправлено', 'Отправлено'),
        ('В обработке', 'В обработке'),
        )
    #id
    #team = models.CharField("Команда-заказчик", max_length=150)
    team = models.ForeignKey(
        Team, verbose_name="Заказчик", on_delete=models.SET_NULL, null=True, blank=True
    )
    products = models.TextField("Заказ", blank=True)
    status = models.CharField("status", max_length=50)
    #models.CharField("форма обучения", max_length=200, choices=STATUS, default=STATUS[1])

    def __str__(self):
        return self.team.name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
