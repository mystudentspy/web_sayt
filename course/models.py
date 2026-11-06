from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Barchasi(TimeStampedModel):
    ism = models.CharField(null=True, blank=True)
    gapir = models.TextField(null=True, blank=True)
    malumot = models.EmailField(null=True, blank=True)
    gap = models.URLField(null=True, blank=True)
    salom = models.IntegerField(null=True, blank=True)
    q = models.SmallIntegerField(null=True, blank=True)
    w = models.BigIntegerField(null=True, blank=True)
    e = models.PositiveIntegerField(null=True, blank=True)
    r = models.FloatField(null=True, blank=True)
    t = models.DecimalField(null=True, blank=True)
    y = models.DateField(null=True, blank=True)
    u = models.TimeField(null=True, blank=True)
    i = models.DateTimeField(null=True, blank=True)
    o = models.DurationField(null=True, blank=True)
    a = models.BooleanField(null=True, blank=True)
    s = models.FileField(null=True, blank=True)