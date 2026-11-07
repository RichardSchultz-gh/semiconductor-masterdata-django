from django.db import models

# Create your models here.

class Lot(models.Model):
    class State(models.TextChoices):
        INIT = "INIT", "Initialisiert"
        WAIT = "WAIT", "Wartet"
        PROC = "PROC", "Wird verarbeitet"
        OP_COMP = "OP_COMP", "Operation abgeschlossen"
        HOLD = "HOLD", "Angehalten"
        FIN = "FIN", "Fertig"
        SCRAP = "SCRAP", "Ausschuss"
    
    lotid = models.CharField(max_length=15, primary_key=True)
    priority = models.IntegerField()
    pieces = models.IntegerField()
    state = models.CharField(max_length=15, choices=State, default=State.INIT)
    product = models.CharField(max_length=15)
    route = models.CharField(max_length=15, blank=True)
    oper = models.CharField(max_length=15, blank=True)
    customer = models.CharField(max_length=15)
    order = models.CharField(max_length=15)
    duedate = models.DateField()
    startdate = models.DateField(null=True, blank=True)
    enteroper = models.DateTimeField(null=True, blank=True)
    procstart = models.DateTimeField(null=True, blank=True)
    disptool = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ["duedate", "lotid"]
        verbose_name = "Los"
        verbose_name_plural = "Lose" 

    def __str__(self):
        return self.lotid

