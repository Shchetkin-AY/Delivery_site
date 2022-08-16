from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    company = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    inn_number = models.IntegerField()
    def __str__(self):
        return self.company

class PackingList(models.Model):
    sender = models.ForeignKey(Agent, related_name='sender', on_delete=models.CASCADE)
    destination = models.ForeignKey(Agent, related_name='destination', on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    weight = models.IntegerField()
    volume = models.IntegerField()
    places_count = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    price = models.IntegerField(null=True, default=0)

    def save(self, *args, **kwargs):
        self.price = self.volume * self.weight * self.places_count
        print(self.price)
        super(PackingList, self).save(*args, **kwargs)



