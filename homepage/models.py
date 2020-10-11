from django.db import models

class Articles(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст') 
    
    def __str__(self):    
        return  '%s: %s-%s' % (self.create_date, self.name, self.text)
        # return  '%s: %s-%s' % (self.create_date, self.update_date,  self.name, self.text)
        
    class Meta:    
        verbose_name='Статью'
        verbose_name_plural='Статьи'

