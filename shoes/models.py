from django.db import models


class Shoe(models.Model):

    GENDER_CHOICES = [
        ("women", "Women"),
        ("men", "Men"),
    ]

    CATEGORY_CHOICES = [
        ("heels", "Heels"),
        ("sneakers", "Sneakers"),
        ("sandals", "Sandals"),
        ("flats", "Flats"),
        ("boots", "Boots"),
        ("formal", "Formal Shoes"),
        ("loafers", "Loafers"),
    ]

    name = models.CharField(
        max_length=200
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="shoes/"
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name