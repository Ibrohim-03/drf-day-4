from django.db import models


class User(models.Model):
    username = models.CharField( max_length=50)
    email = models.CharField( max_length=50)



class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,null=True,blank=True)
    price = models.IntegerField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.TimeField(auto_now_add=True)    



class Review(models.Model):
    text = models.CharField( max_length=50)
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
