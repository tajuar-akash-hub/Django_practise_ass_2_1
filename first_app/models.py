from django.db import models

# Create your models here.
class django_model(models.Model):
    name = models.CharField( max_length=50)
    roll = models.IntegerField(primary_key = True)
    address = models.TextField()

    def __str__(self) -> str:
        return f'name = {self.name}, roll= {self.roll} , address = {self.address}'
