from django.db import models
from django.utils import timezone
from datetime import datetime


class State(models.Model):
    state_name = models.CharField(max_length=200)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Voter(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    u_status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Contestant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200, default=None)
    fathers_name = models.CharField(max_length=200)
    mothers_name = models.CharField(max_length=200)
    contact = models.IntegerField(default=0)
    image = models.ImageField(upload_to="pic/")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    dob = models.DateField()
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    about = models.TextField(max_length=2000)
    hobby = models.CharField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=None)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.first_name

    def num_votes(self):
        return self.vote_set.count()


class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)


class Vote(models.Model):
    contestaant = models.ForeignKey(Contestant, on_delete=models.CASCADE, default=None)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, default=None)
    status = models.IntegerField(default=0)



