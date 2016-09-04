from django.db import models

# Create your models here.
class Battle(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="null")
    year = models.IntegerField()
    battle_number = models.IntegerField()
    attacker_king = models.CharField(max_length=50, default="null")
    defender_king = models.CharField(max_length=50, default="null")
    attacker_1 = models.CharField(max_length=50, default="null")
    attacker_2 = models.CharField(max_length=50, default="null")
    attacker_3 = models.CharField(max_length=50, default="null")
    attacker_4 = models.CharField(max_length=50, default="null")
    defender_1 = models.CharField(max_length=50, default="null")
    defender_2 = models.CharField(max_length=50, default="null")
    defender_3 = models.CharField(max_length=50, default="null")
    defender_4 = models.CharField(max_length=50, default="null")
    attacker_outcome = models.CharField(max_length=50, default="null")
    battle_type = models.CharField(max_length=50, default="null")
    major_death = models.CharField(max_length=50, default="null")
    major_capture = models.CharField(max_length=50, default="null")
    attacker_size = models.CharField(max_length=50, default="null")
    defender_size = models.CharField(max_length=50, default="null")
    attacker_commander = models.CharField(max_length=150, default="null")
    defender_commander = models.CharField(max_length=150, default="null")
    summer = models.CharField(max_length=10, default="null")
    location = models.CharField(max_length=50, default="null")
    region = models.CharField(max_length=50, default="null")
    note = models.CharField(max_length=300, default="null")

    def __str__(self):
        return self.name