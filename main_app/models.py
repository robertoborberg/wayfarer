from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CITIES = (
    ('L', 'London'),
    ('S', 'Sydney'),
    ('T', 'Tokyo'),
    ('P', 'Paris'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    date = models.DateField('Post Date')
    post_city = models.CharField(
        'Post City',
        max_length=10,
        choices=CITIES,
        default=CITIES[0][0]
    )
    
