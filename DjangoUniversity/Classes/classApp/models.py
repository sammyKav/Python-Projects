from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course_Number = models.IntegerField(default=0)
    Instructor_name = models.CharField(max_length=50, default="")
    Duration = models.FloatField(default=0)

    objects = models.Manager()

    def __str__(self):  # this makes it so that you can see attributes of the class when selecting elements of the class
        return self.Title + " " + str(self.Course_Number)
