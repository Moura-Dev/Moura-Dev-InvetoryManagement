from django.db import models

# Create your models here.

class Dispositivo(models.Model):
    tipo = models.CharField(max_length=100, blank=False)
    preco = models.IntegerField()

    escolhas = (
        ('Disponivel', 'Item pronto para venda'),
        ('Vendido', 'Item Vendido'),
        ('Abastecimento', 'Item para repor nos proximos dias')
    )
    status = models.CharField(max_length=100, choices=escolhas, default="Vendido")
    issues = models.CharField(max_length=100, default="Sem problemas")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Tipo : {0} Preco : {1}'.format(self.tipo,self.preco)



class Notebook(Dispositivo):
   pass


class Computador(Dispositivo):
   pass


class Celular(Dispositivo):
   pass
