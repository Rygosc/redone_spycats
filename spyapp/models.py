from django.db import models
from spyapp.validator import valid_breed
from django.utils import timezone


class SpyCat(models.Model):
    name = models.CharField(max_length=50)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=50, validators=[valid_breed])
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Spy cat {self.name}, breed: {self.breed}"


class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Assigned to: {self.cat}"


class Target(models.Model):
    mission = models.ForeignKey(
        Mission, related_name="targets", on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    complete = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["mission", "name"], name="unique_target_per_mission"
            )
        ]

    def save(self, *args, **kwargs):
        if self.complete or self.mission.complete:
            raise ValueError("Cannot update notes for completed mission")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Target: {self.name}. Mission ID: {self.mission.id}. Complete: {self.complete}"
