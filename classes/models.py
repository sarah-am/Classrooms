from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(('M','Male'), ('F','Female')))
    exam_grade = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
    	return ("%s, %s, %s, %s") % (Student.name, Student.date_of_birth, Student.gender, Student.exam_grade)


# date field -> m/d/yyyy