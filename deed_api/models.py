from django.db import models

# Create your models here.

class ExcelData(models.Model):
    tag_name = models.CharField(max_length=100)
    document_name = models.CharField(max_length=100)
    data = models.JSONField()  # Store row data
    created_at = models.DateTimeField(auto_now_add=True)

class FieldPosition(models.Model):
    field_name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    is_global = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.field_name} - ({self.x}, {self.y})"