from django.db import models

# Create your models here.

class Ninja(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(choices=[('Genin','Genin'),('Chunin','Chunin'),('Jonin','Jonin')],max_length=100)

    clan=models.CharField(max_length=50)
    chakra_nature=models.CharField(max_length=50)
    jutsu=models.ManyToManyField("jutsu",related_name="ninjas",blank=True)
    team=models.ForeignKey("Team",on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.name
class Jutsu(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(choices=[('Ninjutsu', 'Ninjutsu'), ('Genjutsu', 'Genjutsu'), ('Taijutsu', 'Taijutsu')], max_length=20)

    def __str__(self):
        return self.name


class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rank =models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)
    assigned_to = models.ManyToManyField(Ninja,related_name='missions')
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
                              max_length=10)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=100)
    leader =models.ForeignKey(Ninja, on_delete=models.SET_NULL, null=True,related_name='team_leader')
    members = models.ManyToManyField('Ninja', related_name='teams')
    def __str__(self):
        return self.name