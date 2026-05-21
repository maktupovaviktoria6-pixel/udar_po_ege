from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=100, verbose_name="Слово (маленькими буквами)")
    stress_index = models.IntegerField(verbose_name="Индекс правильной буквы(с нуля)")
    def __str__(self):
        return self.text
