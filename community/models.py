from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.text import slugify


class communities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    modification_date = models.DateTimeField(editable=False)
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    image = models.ImageField(upload_to='media/community')

    def __str__(self):
        return self.name

    def get_slug(self):
        slug = slugify(self.name.replace("ı", "i"))
        unique = slug
        number = 1

        while communities.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug,number)
            number += 1

        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            creation_date = timezone.now
        self.modification_date = timezone.now()
        self.slug = self.get_slug()
        return super(communities, self).save(*args, **kwargs)
