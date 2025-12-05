from django.db import models
from django.contrib.auth.models import User


class ActivityCategory(models.Model):
    name = models.CharField(max_length=100)          # e.g. Electricity, Car Travel
    unit = models.CharField(max_length=50)           # e.g. kWh, km, meal
    emission_factor = models.FloatField(             # kg CO2 per unit
        help_text="kg CO₂ per unit"
    )

    def __str__(self):
        return f"{self.name} ({self.unit})"


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    amount = models.FloatField()                     # how many units (e.g. 10 kWh)
    date = models.DateField()

    @property
    def emissions(self):
        # total kg CO2 for this activity
        return self.amount * self.category.emission_factor

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.amount} {self.category.unit}"
