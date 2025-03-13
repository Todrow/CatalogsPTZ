from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):

    ADMIN = "AD"
    USER = "US"
    CATALOG = "CG"
    ROLES_CHOICES = {
        ADMIN: "Admin",
        USER: "User",
        CATALOG: "Catalog",
    }
    role = models.CharField(
        max_length=2,
        choices=ROLES_CHOICES,
        default=USER
    )

    def __str__(self):
        return f'Profile the {self.username}, with role: {self.role}'


class Detail(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    assembly_disignation = models.CharField(max_length=255)
    note = models.TextField()
    link = models.TextField()
    folder = models.ManyToManyField(
        to="api.Folder", verbose_name=("parent is folder"), related_name='details')

    def __str__(self):
        return f'Name is: {self.name}, the parent is: {self.folder}'


class Folder(models.Model):
    tag = models.CharField(max_length=4)
    VIN = models.CharField(max_length=50, null=True)
    description = models.TextField()
    parent = models.ManyToManyField("api.Folder", verbose_name=(
        "parent"), blank=True, related_name='childs')

    def __str__(self):
        return f'{self.tag} with VIN: {self.VIN}'


class IMG(models.Model):
    folder = models.OneToOneField(
        "api.Folder", on_delete=models.CASCADE, related_name='IMG')
    path = models.TextField((""), blank=False)

    def __str__(self):
        return str(str(self.folder) + ": " + self.path)


class Hot_point(models.Model):
    folder_link = models.ForeignKey(
        "api.Folder", on_delete=models.CASCADE, related_name='hot_points')
    coordinates = ArrayField(base_field=models.IntegerField(("")), size=2)
    IMG = models.ForeignKey(
        "api.IMG", on_delete=models.CASCADE, related_name='hot_points')
    text = models.TextField((""))

    def __str__(self):
        return f'The {self.text} in coords: {self.coordinates}, in IMG {self.IMG}'


class Count_details(models.Model):
    folder = models.OneToOneField(
        "api.Folder", on_delete=models.CASCADE, related_name='count_details')
    detail = models.OneToOneField(
        "api.Detail", on_delete=models.CASCADE, related_name='count_details')
    count = models.SmallIntegerField((""))

    def __str__(self):
        return f'In {self.folder} details "{self.detail}" = {self.count}'
