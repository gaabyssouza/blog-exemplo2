from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    título = models.CharField(max_length=140)
    subtítulo = models.CharField(max_length=140, blank=True)
    data_criacao = models.DateTimeField(auto_now_add= True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.título