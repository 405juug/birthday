from django.db import models

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'