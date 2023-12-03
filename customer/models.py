from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='items')  # Fix the related_name

    def __str__(self):  # Fix the method name
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # Fix the method name
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(MenuItem, related_name='orders', blank=True) # Fix the related_name
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pincode = models.IntegerField(blank=True, null=True)
    def __str__(self):  # Fix the method name
        return f'Order: {self.created_on.strftime("%b %d %I:%M %p")}'
