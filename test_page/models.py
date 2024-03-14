from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True)
    profile_creation_time = models.DateTimeField(default=timezone.now())
    last_visit_time = models.DateTimeField(blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True)


class Question(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'M', 'Moderation'
        PUBLISHED = 'P', 'Published'

    class Language(models.TextChoices):
        Python = 'P', 'Python'
        JavaScript = 'JS', 'JavaScript'
        Java = 'J', 'Java'
        Typescript = 'T', 'Typescript'
        C = 'C#', 'C#'
        PHP = 'PHP', 'PHP'


    language = models.CharField(max_length=30, choices=Language.choices)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    added_by_user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()


    def __str__(self):
        return self.title

class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    uset_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']


