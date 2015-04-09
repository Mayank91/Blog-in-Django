from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_id = models.EmailField()
    date = models.DateTimeField(default = 0)

    def __str__(self):
        return (self.first_name)

