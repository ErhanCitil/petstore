from django.db import models

# Create your models here.
class Pet(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE, related_name='pet')
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, related_name='pet')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    skin_color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name

class Image(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.id
    
class Breed(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name