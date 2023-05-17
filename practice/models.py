from django.db import models

# Create your models here.
from django.db import models

from datetime import date




class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

   


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


# Create your models here.

class Teacher(models.Model):  
    teacher_name = models.CharField(max_length=200)  
  
    def __str__(self):  
        return f'{self.teacher_name}' 
    

class Student(models.Model):  
    username = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.IntegerField()  
    email = models.EmailField()  
    teacher_name = models.ForeignKey(Teacher, blank = True, null = True, on_delete= models.CASCADE)
  
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)
    

class jobs(models.Model):
    job_name = models.CharField(max_length=100)



# abstaract-base class inheritence
class VehicleInfo(models.Model):
    name = models.CharField(max_length=20)
    colour = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Vehicle(VehicleInfo):
    customer = models.ForeignKey(Student,related_name='vehicle',on_delete=models.CASCADE)


# multi-table inheritence
class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Location):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


# proxy model inheritence
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)


class MyBook(Book):

    class Meta:
        proxy = True
        ordering = ["title"]


# ordering in Meta class
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)
    

class Brocamp(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)