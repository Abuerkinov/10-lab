from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    datetime = models.DateTimeField(auto_now=True)
    is_view = models.IntegerField(default=0)

    def __str__(self):
        return self.name
