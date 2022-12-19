from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 150)

    def __str__(self):
        return "User: %s email: %s" % (self.name, self.email)