from django.db import models

class Alunos(models.Model):
    turma = models.CharField(max_length=100)
    sala = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
        
