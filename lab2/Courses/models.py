from django.db import models
from utils.base_model import BaseModel

# Create your models here.
class Course(BaseModel):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.title}"
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'