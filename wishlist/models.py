from django.db import models

from products.models import Product

class WishlistItem(models.Model):
    session_key=models.CharField(max_length=40)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wishlist_items')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('session_key','product')
        ordering=['-created_at']

    def __str__(self):
        return f"{self.session_key}-{self.product.name}"    