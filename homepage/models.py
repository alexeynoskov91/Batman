from django.db import models

class Articles(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст') # как в админке ограничить вывод текста статьи?
    
    # url = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):    
        return  '%s: %s-%s' % (self.create_date,  self.name, self.text)
    
    class Meta:    
        verbose_name='Статью'
        verbose_name_plural='Статьи'

