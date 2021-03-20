from django.db import models
from django.utils.timezone import now

# Create your models here.


class Quality_rating(models.Model):
    ticket_id = models.IntegerField()
    rating = models.IntegerField()
    created_date = models.DateTimeField(default=now, editable=False)
    comment = models.TextField() 
    user = models.TextField( null=True) 
    resolution_time = models.TextField( null=True) 