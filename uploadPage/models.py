from django.db import models

class DailyRecord(models.Model):
    image_url = models.URLField()  # Store the URL of the uploaded image
    description = models.TextField(blank=True)  # Store the associated description
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Daily Record {self.id} - {self.description[:20]}..."  # Show a snippet of the description
