from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.


class Protest(models.Model) :
    TYPE_CHOICES = (
        ('a', '집회'),
        ('b', '서명운동'),
        ('c', '전시'),
        ('d', '플래시몹'),
        ('e', '기타'),
    )
    type_of = models.CharField(max_length=50, choices = TYPE_CHOICES, default='a')
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    place = models.TextField()
    number_of_people = models. PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ])
    user = models.ForeignKey('User')
    def __str__(self):
        return self.title



class User(models.Model):
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=200)

    def __str__(self) :
        return self.nickname



class Participation(models.Model):
    protest = models.ForeignKey(Protest)
    user = models.ForeignKey(User)



