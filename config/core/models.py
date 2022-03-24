from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from graphql import GraphQLError

from .services import generate_slug


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class URL(BaseModel):
    full_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            while not self.short_url:
                generate_url = generate_slug(6)
                try:
                    url = URL.objects.get(short_url=generate_url)
                except ObjectDoesNotExist:
                    self.short_url = generate_url

        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            raise GraphQLError('invalid url')

        return super().save(*args, **kwargs)
