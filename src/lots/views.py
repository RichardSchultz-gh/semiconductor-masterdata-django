from django.shortcuts import get_object_or_404, redirect, render
from lots.forms import LotForm
from lots.models import Lot


def lot_edit(request, lotid):
    lot = get_object_or_404(Lot, lotid=lotid)

    if request.method == "POST":
        form = LotForm(request.POST, instance=lot)
        if form.is_valid():
            form.save()
            return redirect("lots:lot_edit", lotid=lot.lotid)
    else:
        form = LotForm(instance=lot)

    return render(request, "lots/lot_edit.html", {"lot": lot, "form": form})

def lot_list(request):
    lots = Lot.objects.all()
    
    lotid = request.GET.get("lotid", "").strip()
    state = request.GET.get("state", "")

    if lotid:
        lots = lots.filter(lotid__icontains=lotid)
    if state:
        lots = lots.filter(state=state)

    return render(request, "lots/lot_list.html", {
        "lots": lots,
        "lotid": lotid,
        "states": Lot.State.choices,
        "state": state,
    })
