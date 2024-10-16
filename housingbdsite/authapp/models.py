from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    artist = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()

    rating = (
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Not Bad'),
        (4, 'Good'),
        (5, 'Best'),
        
    )
    num_star = models.IntegerField(choices=rating)

    def __str__(self):
        return f"{self.name}, Rating: {self.num_star} stars"
