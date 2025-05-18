# models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name




class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()  # ✅ Add this line
    address = models.TextField()
    items = models.ManyToManyField('MenuItem')
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    payment_method = models.CharField(max_length=50, choices=[
        ('Cash on Delivery', 'Cash on Delivery'),
        ('UPI', 'UPI'),
        ('Card', 'Credit/Debit Card'),
    ])
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    ordered_items = models.TextField()  # could also be ManyToManyField if structured
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name}"




