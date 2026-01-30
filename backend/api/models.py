from django.db import models

class Country(models.Model):
    MAX_LENGTH_COUNTRY_NAME = 100

    name = models.CharField(unique=True, max_length=MAX_LENGTH_COUNTRY_NAME)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class League(models.Model):
    MAX_LENGTH_LEAGUE_NAME = 100

    name = models.CharField(unique=True, max_length=MAX_LENGTH_LEAGUE_NAME)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    MAX_LENGTH_CHARACTERISTICS_NAME = 100

    name = models.CharField(unique=True, max_length=MAX_LENGTH_CHARACTERISTICS_NAME)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FootballClub(models.Model):
    MAX_FOOTBALL_CLUB_NAME_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 100
    MAX_CITY_NAME_LENGTH = 100

    name = models.CharField(unique=True, max_length=MAX_FOOTBALL_CLUB_NAME_LENGTH)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)
    attendance = models.IntegerField(null=True)
    city = models.CharField(max_length=MAX_CITY_NAME_LENGTH)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    characteristic = models.ManyToManyField(Characteristic)


    def __str__(self):
        return self.name