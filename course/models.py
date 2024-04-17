from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField("media/course/speciality/")
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
    class PriceType(models.TextChoices):
        dollar = "USD", "$"
        sum = "UZS", "so'm"

    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField("media/course/course/")
    active_users = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    price_type = models.CharField(max_length=50, choices=PriceType.choices, default=PriceType.sum)
    rating = models.FloatField()
    speciality = models.ManyToManyField(Speciality)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Position(models.Model):
    name = models.CharField(max_length=100)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/course/teacher/")
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

