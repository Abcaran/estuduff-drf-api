from django.db import models


class Modality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=70)
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudyProfile(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class StudyPlaceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Campus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=40)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudyPlace(models.Model):
    name = models.CharField(max_length=50)
    complement = models.CharField(max_length=70)
    latitude = models.FloatField()
    longitude = models.FloatField()
    studyProfile = models.ManyToManyField('StudyProfile')
    studyPlaceType = models.ForeignKey(
        StudyPlaceType, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    studyProfile = models.ForeignKey(StudyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
