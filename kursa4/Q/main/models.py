import datetime

from django.db import models
from django.urls import reverse

def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]

class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Ноутбуки': 'notebook__count',
        'Смартфоны': 'smartphone__count'
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count('notebook', 'smartphone')
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url, count= getattr(c,self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data




class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})


class Question(models.Model):
    title = models.CharField('Тема вопроса', max_length=50)
    describe = models.TextField('Текст вопроса')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Feedback(models.Model):
    title = models.CharField('Название', max_length=50)
    describe = models.TextField('Описание')
    mark = models.PositiveSmallIntegerField('Оценка', max_length=1)
    date = datetime.datetime.now()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class News(models.Model):
    title = models.CharField('Название', max_length=50)
    describe = models.TextField('Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

