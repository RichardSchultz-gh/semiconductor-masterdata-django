from django.contrib import admin
from lots.models import Lot


class LotAdmin(admin.ModelAdmin):
    list_display = [
        "lotid",
        "state",
        "priority",
        "pieces",
        "product",
        "customer",
        "order",
        "route",
        "oper",
        "duedate",
        "startdate",
    ]
    list_filter = ["state", "customer", "duedate"]
    search_fields = ["lotid", "customer", "order"]


# Register your models here.
admin.site.register(Lot, LotAdmin)

