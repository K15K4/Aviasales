from django.db import models


class Airplane(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    countryEnd = models.ForeignKey(Country, on_delete=models.PROTECT)
    airplane = models.ForeignKey(Airplane, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    description = models.FileField(upload_to='files/')
