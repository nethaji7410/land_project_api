from django.db import models

# Create your models here.

class ExcelData(models.Model):
    tag_name = models.CharField(max_length=100) #Stores a tag/category name for the document
    document_name = models.CharField(max_length=100) # Stores the name of the document
    data = models.JSONField()  # Store row data
    created_at = models.DateTimeField(auto_now_add=True)

class FieldPosition(models.Model):
    field_name = models.CharField(max_length=100) # # Stores the name of the field
    x = models.FloatField()
    y = models.FloatField()
    is_global = models.BooleanField(default=False) #If True, this position applies globally ,Use only for a specific form/template
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.field_name} - ({self.x}, {self.y})"