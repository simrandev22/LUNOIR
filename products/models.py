from django.db import models

class Category(models.Model):

    SECTION_CHOICES=[("clothing","Clothing"),
                     ("shoes","Shoes"),
                     ("makeup","Makeup"),]


    GROUP_CHOICE=[("women","Women"),
                  ("men","Mens"),
                  ("face","Face"),
                  ("eyes","Eyes"),
                  ("lips","Lips")]

    name=models.CharField(max_length=100)

    section=models.CharField(max_length=20,choices=SECTION_CHOICES)

    group=models.CharField(max_length=20,choices=GROUP_CHOICE)

    slug=models.SlugField(max_length=120,unique=True)

    def __str__(self):
        return f"{self.get_section_display()} → {self.get_group_display()} → {self.name}"

class Product(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name