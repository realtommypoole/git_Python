from django.db import models

class djangoClasses (models.Model):
    title = models.CharField(max_length=60, null=False)
    CourseNumber = models.IntegerField(max_length=60, null=False)
    InstructorName = models.CharField(max_length=60)
    Duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.title