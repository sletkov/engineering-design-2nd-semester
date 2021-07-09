import datetime

from django.db import models




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

