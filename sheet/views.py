from django.shortcuts import render
from .models import Sheet
# Create your views here.


def sheets(request):
    sheets = Sheet.objects.all()

    return render(request, './sheet/sheets.html', {'sheets': sheets})
