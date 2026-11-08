from django import forms
from lots.models import Lot

class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = ["priority",
                  "pieces",
                  "state",
                  "product",
                  "route",
                  "oper",
                  "customer",
                  "order",
                  "duedate",
                  "startdate",
                  "enteroper",
                  "procstart",
                  "disptool" ]
        widgets = {
            "duedate":   forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "startdate": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "enteroper": forms.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local"}),
            "procstart": forms.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local"}),
        }
