from django.db import models

class Collect(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование идеи')
    description = models.TextField(blank=True, verbose_name='Описание текущей ситуации (недостатки)')
    offer = models.TextField(blank=True, verbose_name='Предложение по улучшению')
    result = models.TextField(blank=True, verbose_name='Ожидаемый результат')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания' )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'
        ordering = ['-created_at']


