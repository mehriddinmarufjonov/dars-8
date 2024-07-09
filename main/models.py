from django.db import models

class Type(models.Model):
    name  = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Food(models.Model):
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)
    price = models.IntegerField()


    def __str__(self):
        return self.name
    
class Comment(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
