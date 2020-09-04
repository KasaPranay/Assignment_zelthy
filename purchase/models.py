from django.db import models

# Create your models here.
class PurchaseModel(models.Model):
    purchaser_name = models.CharField(max_length = 20)
    quantity = models.IntegerField()

class PurchaseStatusModels(models.Model):
    purchase = models.ForeignKey(PurchaseModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=(
        ('open', 'Open'),
        ('verified', 'Verified'),
        ('dispatched','Dispatched'),
        ('delivered','Delivered')))
    created_at = models.DateTimeField(auto_now_add=True)