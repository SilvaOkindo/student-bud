from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(default=0)


class Subject(models.Model):
    name = models.CharField(max_length=30)


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    reputation = models.IntegerField(default=0)
    expertise = models.ManyToManyField(Subject)


class Category(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    deadline = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')


class Solution(models.Model):
    assignment = models.OneToOneField(Assignment, on_delete=models.CASCADE)
    solution = models.TextField()
    attachments = models.ManyToManyField(Attachment)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    is_brainliest = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    asked_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    view_count = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)


class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField()
    comment = models.TextField()


class ChatMessage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
