from django.db import models

class GymUser(models.Model):
    # Basic Details
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True) # Unique ensures no duplicates
    location = models.CharField(max_length=200)
    
    # Gym Stats
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # e.g., 75.50
    joining_date = models.DateField()
    
    # Subscription Details
    subscription_start_date = models.DateField()
    subscription_end_date = models.DateField()
    trainer_name = models.CharField(max_length=100, null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.mobile_number}"
