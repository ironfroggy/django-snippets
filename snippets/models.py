from django.db import models

class Snippet(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, default="")
    body = models.TextField(default="")

    def __unicode__(self):
        return "Snippet '%s'" % (self.title,)

