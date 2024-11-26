from django.db import models
from spyapp.validator import valid_breed


class SpyCat(models.Model):
    name = models.CharField(max_length=50)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(
        max_length=50, validators=[valid_breed]
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Spy cat {self.name}, breed: {self.breed}"
