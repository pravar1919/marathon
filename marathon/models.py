from django.db import models


class Orders(models.Model):
    name = models.CharField(max_length=220)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    get_tshirt = models.BooleanField(default=False)
    # payment_status = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)