from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    student_age = models.IntegerField()
    def __str__(self):
        return self.student_name

