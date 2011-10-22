from django.db import models


class Brewery(models.Model):

    """
    Brewery model.
    """

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='brewery/')
    website = models.CharField(max_length=200) # Apparently the URLField type
                                               # has been deprecated as of
                                               # Django 1.3.1, but it is
                                               # unclear what should be used
                                               # instead. CharField makes as
                                               # much sense as anything.

    def __unicode__(self):
        return self.name


class Beer(models.Model):

    """
    Beer model.
    """

    name = models.CharField(max_length=100)
    brewery = models.ForeignKey(Brewery)
    style = models.CharField(max_length=25)
    pic = models.ImageField(upload_to='beer/')
    abv = models.FloatField()

    def __unicode__(self):
        return self.name


class Review(models.Model):

    """
    Beer review model.
    """

    CONTAINER_CHOICES = (
        ('CAN', 'Can'),
        ('BTL', 'Bottle'),
        ('TAP', 'Draught'),
        ('CSK', 'Cask'),
        ('GLR', 'Growler'),
        ('OTR', 'Other'),
    )

    beer = models.ForeignKey(Beer)
    date = models.DateField()
    content = models.TextField()
    rating = models.PositiveIntegerField()
    pic = models.ImageField(upload_to='review/')
    container = models.CharField(max_length=3, choices=CONTAINER_CHOICES)
    volume = models.CharField(max_length=15)

    def __unicode__(self):
        return '{0} / {1}'.format(self.beer, self.date)
