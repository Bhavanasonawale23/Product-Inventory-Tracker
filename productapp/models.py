from django.db import models

# Create your models here.

class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()

    # def __str__(self):
    #     return self.pname

    # def __str__(self):
    #     return f"{self.pname} ({self.category}) - ${self.price}, Qty: {self.qty}"

    def __str__(self):
        return self.pname +  "-" + self.category


