from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model): # Class car esta herdando a herança da (Class Model) - já esta pronta 
    # Escrever os campos da tabela
    id = models.AutoField(primary_key=True) # id de cada carro cadastrado
    model = models.CharField(max_length=200) # modelo do carro - 
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # marca do carro
    factory_year = models.IntegerField(blank=True, null=True) # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True)  # ano do modelo
    plate = models.CharField(max_length=10, blank=True, null= True) # Placa do carro
    value = models.FloatField(blank=True, null=True) # valor 
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # Imagem/fotos


    def __str__(self):
        return self.model
    
