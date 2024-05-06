from django.db import models

# Create your models here.


class Login(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)


class Trainer(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Age = models.IntegerField()
    Experience = models.IntegerField()
    Gender = models.CharField(max_length=20)
    Place = models.CharField(max_length=20)
    Post = models.CharField(max_length=20)
    Pin = models.IntegerField()
    Phone = models.BigIntegerField()
    Email = models.CharField(max_length=20)
    Photo = models.FileField()
    LOGIN_ID = models.ForeignKey('Login', on_delete=models.CASCADE)


class User(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20)
    Weight = models.CharField(max_length=20)
    Height = models.CharField(max_length=20)
    Place = models.CharField(max_length=20)
    Post = models.CharField(max_length=20)
    Pin = models.IntegerField()
    Phone = models.BigIntegerField()
    Email = models.CharField(max_length=20)
    Photo = models.FileField()
    LOGIN_ID = models.ForeignKey('Login', on_delete=models.CASCADE)


class Attendance(models.Model):
    Date = models.CharField(max_length=20)
    Attendance = models.CharField(max_length=20)
    LOGIN_ID = models.ForeignKey(Login, on_delete=models.CASCADE)


class Food(models.Model):
    FoodName = models.CharField(max_length=30)
    FoodType = models.CharField(max_length=30)
    Time = models.CharField(max_length=20)
    Quantity = models.CharField(max_length=20)


class Exercise(models.Model):
    ExerciseName = models.CharField(max_length=50)
    ExerciseType = models.CharField(max_length=50)
    ExerciseDetails = models.CharField(max_length=100)
    ExerciseVideo = models.FileField()


class Feedback(models.Model):
    Date = models.CharField(max_length=20)
    FeedbackUser = models.CharField(max_length=100)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)


class Assign(models.Model):
    Date = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    TRAINER_ID = models.ForeignKey(Trainer, on_delete=models.CASCADE)


class Complaints(models.Model):
    Complaint = models.CharField(max_length=100)
    Date = models.CharField(max_length=20)
    Reply = models.CharField(max_length=100)
    USER_ID = models.ForeignKey('User', on_delete=models.CASCADE)


class Progress(models.Model):
    Date = models.CharField(max_length=20)
    Weight = models.CharField(max_length=20)
    Height = models.CharField(max_length=20)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)


class DietChart(models.Model):
    Chart = models.FileField()
    Description = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    TRAINER_ID = models.ForeignKey(Trainer, on_delete=models.CASCADE)


class Tips(models.Model):
    Tip = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    TRAINER_ID = models.ForeignKey(Trainer, on_delete=models.CASCADE)


class Videos(models.Model):
    Video = models.FileField()
    Description = models.CharField(max_length=100)
    Date = models.CharField(max_length=20)
    Title = models.CharField(max_length=100)
    TRAINER_ID = models.ForeignKey(Trainer, on_delete=models.CASCADE)

