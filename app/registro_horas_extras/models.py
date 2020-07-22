from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=70, help_text='Motivo da extra')

    def __str__(self):
        return self.motivo
