from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # For longer text descriptions
    updated_on = models.DateTimeField(auto_now=True)
    # Add other relevant fields like images, authors, etc.

    def __str__(self):
        return self.title