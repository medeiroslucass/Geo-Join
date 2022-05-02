from django.db import models

class Alvo(models.Model):
    nome = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    data_expiracao = models.DateField(null=True, blank=True)


    def __str__(self) -> str:
        return self.nome

    def to_dict(self):
        return {
            'id' : self.id,
            'nome' : self.nome,
            'latitude' : self.latitude,
            'longitude' : self.longitude,
            'data_expiracao' : self.data_expiracao,
        }


class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address