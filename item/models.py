from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings

MEDIA_TYPE_CHOICES = [
    ('DVD', 'DVD'),
    ('BLU', 'Blu-ray'),
    ('4K', '4K Blu-ray'),
]

BBFC_CHOICES = [
    ('U', 'U'),
    ('PG', 'PG'),
    ('12', '12'),
    ('15', '15'),
    ('18', '18'),
]


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BoxSet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Media(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = CloudinaryField('image', blank=True, null=True)
    media_type = models.CharField(max_length=3, choices=MEDIA_TYPE_CHOICES)
    year = models.PositiveIntegerField(blank=True, null=True)
    boxset = models.ForeignKey(BoxSet, on_delete=models.SET_NULL, blank=True, null=True, related_name='media_items')
    bbfc_rating = models.CharField(max_length=2, choices=BBFC_CHOICES, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.media_type}) - {self.year if self.year else 'Unknown Year'}"