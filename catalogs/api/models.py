from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Detail(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    assembly_disignation = models.CharField(max_length=255)
    note = models.TextField()
    link = models.TextField()
    folder = models.ManyToManyField("api.Folder", verbose_name=("parent is folder"))

    def __str__(self):
        return f'Name is: {self.name}, the parent is: {self.folder}'

class Folder(models.Model):
    tag = models.CharField(max_length=4)
    VIN = models.CharField(max_length=50, null=True)
    description = models.TextField()
    parent = models.ManyToManyField("api.Folder", verbose_name=("parent"))

    def __str__(self):
        return f'{self.tag} with VIN: {self.VIN}'
    

class IMG(models.Model):
    folder = models.OneToOneField("api.Folder", on_delete=models.CASCADE)
    path = models.TextField((""))

    def __str__(self):
        return str(str(self.folder) + ": " + self.path)
    

class Hot_point(models.Model):
    folder_link = models.ForeignKey("api.Folder", on_delete=models.CASCADE)
    coordinates = ArrayField(base_field=models.IntegerField(("")), size=2)
    IMG = models.OneToOneField("api.IMG", on_delete=models.CASCADE)
    text = models.TextField((""))

    def __str__(self):
        return f'The {self.text} in coords: {self.coordinates}, in IMG {self.IMG}'


class Count_details(models.Model):
    folder = models.OneToOneField("api.Folder", on_delete=models.CASCADE)
    detail = models.OneToOneField("api.Detail", on_delete=models.CASCADE)
    count = models.SmallIntegerField((""))

    def __str__(self):
        return f'In {self.folder} details "{self.detail}" = {self.count}'
