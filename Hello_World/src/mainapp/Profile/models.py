from django.db import models

PREFIX_CHOICES = {
                  ('Mr.', 'Mr.'),
                  ('Ms.', 'Ms.'),
                  ('non-binary', 'non-binary')
                  }


class Profile(models.Model):
    Prefix = models.CharField(max_length=20, choices=PREFIX_CHOICES, null=True)
    First_Name = models.CharField(max_length=60)
    Last_Name = models.CharField(max_length=60)
    Email = models.CharField(max_length=70)
    UserName = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name

