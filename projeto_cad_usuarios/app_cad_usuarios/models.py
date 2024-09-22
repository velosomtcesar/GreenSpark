from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)  # Nome de usuário
    senha = models.CharField(max_length=255)  # Campo para armazenar a senha (criptografada)
