from django.db import models
from django.urls import reverse


class Page(models.Model):
    '''простые страницы'''
    name = models.CharField("Название", max_length=100)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"