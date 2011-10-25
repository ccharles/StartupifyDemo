from datetime import datetime

from django.db import models


class Brewery(models.Model):

    """
    Brewery model.
    """

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='brewery/', blank=True)

    # Apparently the URLField type has been deprecated as of Django 1.3.1,
    # but it is unclear what should be used instead. CharField makes as much
    # sense as anything.
    website = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Breweries'

    def __unicode__(self):
        return self.name


class Beer(models.Model):

    """
    Beer model.
    """

    name = models.CharField(max_length=100)
    brewery = models.ForeignKey(Brewery)
    style = models.CharField(max_length=25)
    pic = models.ImageField(upload_to='beer/', blank=True)
    abv = models.FloatField(verbose_name='ABV')
    beeradvocate_rating = models.CharField(max_length=10, blank=True)
    ratebeer_rating = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.name

    def external_rating(self):
        """
        Return a string combining the RateBeer and BeerAdvocate ratings.

        If either rating is unavailable, use 'N/A'.
        """
        return 'BA: {0}, RB: {1}'.format(self.beeradvocate_rating or 'N/A',
                                         self.ratebeer_rating or 'N/A')


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
    date = models.DateField(default=datetime.now())
    content = models.TextField()
    rating = models.PositiveIntegerField()
    pic = models.ImageField(upload_to='review/', blank=True)
    container = models.CharField(max_length=3, choices=CONTAINER_CHOICES,
                                 verbose_name='Format')
    volume = models.CharField(max_length=15)

    def __unicode__(self):
        return '{0} / {1}'.format(self.beer, self.date)


class ReviewComment(models.Model):

    """
    Model for a comment on a review.
    """

    class Meta:
        verbose_name = 'Comment'

    review = models.ForeignKey(Review)
    author = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __unicode__(self):
        return 'Comment on {0}'.format(self.review)
