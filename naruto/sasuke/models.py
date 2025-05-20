from django.db import models

# Create your models here.

class Ninja(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(choices=[('Genin','Genin'),('Chunin','Chunin'),('Jonin','Jonin')],max_length=100)
    clan=models.CharField(max_length=50)
    chakra_nature=models.CharField(max_length=50)
    jutsu=models.ManyToManyField("jutsu",blank=True)
    team=models.ForeignKey("Team",on_delete=models.SET_NULL,null=True,blank=True)

class Jutsu(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(choices=[('Ninjutsu', 'Ninjutsu'), ('Genjutsu', 'Genjutsu'), ('Taijutsu', 'Taijutsu')], max_length=20)
    chakra_cost = models.IntegerField()

class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rank =models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)
    assigned_to = models.ManyToManyField(Ninja)
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
                              max_length=10)

class Team(models.Model):
    name = models.CharField(max_length=100)
    leader =models.ForeignKey(Ninja, on_delete=models.SET_NULL, null=True,related_name='team_leader')