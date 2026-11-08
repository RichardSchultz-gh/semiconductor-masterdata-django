from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
import csv
from lots.models import Lot

def aware_datetime(value):
    if value == "":
        return None
    
    dt = parse_datetime(value)
    if dt is not None:
        dt = make_aware(dt)
    return dt

class Command(BaseCommand):
    help = "Importiert Lose aus LOT.csv"
    
    def add_arguments(self, parser):
        parser.add_argument("csv_path")
    

    def handle(self, *args, **options):
        csv_path = options["csv_path"]
        with open(csv_path, newline="", encoding="utf-8") as f:
            num_created = num_updated = 0
            
            for row in csv.DictReader(f):
                obj, created = Lot.objects.update_or_create(
                        lotid=row["LOTID"],
                        defaults={
                            "priority": row["PRIORITY"],
                            "pieces":   row["PIECES"],
                            "state":    row["STATE"],
                            "product":  row["PRODUCT"],
                            "route":    row["ROUTE"],
                            "oper":     row["OPER"],
                            "customer": row["CUSTOMER"],
                            "order":    row["ORDER"],
                            "duedate":  row["DUEDATE"],    
                            "startdate":row["STARTDATE"] or None,
                            "enteroper":aware_datetime(row["ENTEROPER"]),
                            "procstart":aware_datetime(row["PROCSTART"]),
                            "disptool": row["DISPTOOL"]
                        })
                if created: 
                    num_created += 1
                else: 
                    num_updated += 1
            self.stdout.write(self.style.SUCCESS(f"created: {num_created} updated: {num_updated}"))

