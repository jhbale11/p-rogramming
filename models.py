from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class Protest(models.Model) :
    type_of = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    place = models.TextField()
    number_of_people = models. PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(1001),
            MinValueValidator(1)
        ])
    user_id = models.ForeignKey('blog.User')
    def __str__(self):
        return self.title

class User(models.Model):
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    def __str__(self) :
        return self.nickname

class Participation(models.Model):
    protest_name = models.ForeignKey('blog.Protest')
    user_id = models.ForeignKey('blog.User')
