from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    img = CloudinaryField('image')
    # img = models.ImageField(upload_to="signsImage")
    desc = models.TextField()
    order = models.IntegerField()
    favor = models.BooleanField(default=False)

