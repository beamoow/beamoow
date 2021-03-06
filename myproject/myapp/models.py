# from unicodedata import category
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.dispatch import receiver
# from django.urls import reverse



# class Category(models.Model):
#         CATEGORYCHOICE = [
#         ("Gentleman", "Gentleman"),
#         ("Ladies", "Ladies"),
#         ("Children", "Children"),
#         ("Necklace", "Necklace"),
#         ("Bracelets", "Bracelets"),
#         ("Ring", "Ring"),
#         ("Earrings", "Earrings"),
#         ("Bags", "Bags"),
#         ("Glasses", "Glasses"),
#         ("Shoes", "Shoes"),
#         ("Hats", "Hats"),
#         ]
        
#         namecategory = models.CharField(max_length=50, choices = CATEGORYCHOICE, null=True)
#         slug = models.SlugField(max_length=50, unique=True, null=True)

#         class Meta:
#             verbose_name_plural = 'categories'

#         def get_absolute_url(self):
#             return reverse('store:category_list', args=[self.slug])

#         def __str__(self):
#             return self.namecategory





class Product(models.Model):
    COLORCHOICE = [
        ("white", "white"),
        ("black" , "black"), 
        ("yellow", "yellow"),
        ("red", "red"),
        ("orange", "orange"),
        ("pink", "pink"),
        ("violet", "violet"),
        ("green", "green"),
        ("blue", "blue"),
        ("Sky blue", "Sky blue"),
        ("beige", "beige"),
        ("brown", "brown"),
        ("Silver", "Silver"),
        ]  
    CATEGORYCHOICE = [
        ("Gentleman", "Gentleman"),
        ("Ladies", "Ladies"),
        ("Children", "Children"),
        ("Necklace", "Necklace"),
        ("Bracelets", "Bracelets"),
        ("Ring", "Ring"),
        ("Earrings", "Earrings"),
        ("Bags", "Bags"),
        ("Glasses", "Glasses"),
        ("Shoes", "Shoes"),
        ("Hats", "Hats"),
        ]
    seller = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'myimages')
    # slug = models.SlugField(max_length=50, unique=True, null=True)
    category = models.CharField(max_length=50, choices = CATEGORYCHOICE, null=True)
    # category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    color = models.CharField(max_length=20, choices = COLORCHOICE, null=True)
    size = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "%s %s %s %s %s %s"%(self.pk, self.name, self.quantity, self.price, self.color, self.size)





class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, unique=True, null=True, blank=True)
    Firstname = models.CharField(max_length=50, null=True)
    Lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    DOB = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    tel = models.CharField(max_length=15, blank=True)

    # def get_absolute_url(self):
    #     return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return "%s %s"%(self.pk, self.user)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('update_profile_signal: create a profile')





class Purchase(models.Model):
    PAYCHOICE = [
        ("Promptpay" , "Promptpay"), 
        ("credit/debit", "credit/debit"), 
        ]  
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    coupon = models.CharField(max_length=20)
    payment = models.CharField(max_length=30, choices = PAYCHOICE, default="Promptpay")



class Review(models.Model):
    RATINGCHOICE = [
        ("1" , "1"), 
        ("2", "2"), 
        ("3", "3"), 
        ("4", "4"), 
        ("5", "5")
        ]
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)    
    ratings = models.CharField(max_length=2,choices = RATINGCHOICE, default="5")
    comment = models.CharField(max_length=100)