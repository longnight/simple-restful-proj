from django.db import models


class Rest(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.URLField()

    def __unicode__(self):
        return self.email
