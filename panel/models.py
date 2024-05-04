from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length = 100, null=True)
    email = models.EmailField()
    mobile_num = models.CharField(max_length = 10)
    city = models.CharField(max_length = 100)
    customer_id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False)