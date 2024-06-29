from django.db import models



class Klass(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=100)
    conten = models.TextField()
    period = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    klass = models.ForeignKey(Klass,on_delete=models.CASCADE,related_name='klass')
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='hotel')

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name