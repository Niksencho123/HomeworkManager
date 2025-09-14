from django import forms
from . import models
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime

class AssignmentAdd(forms.ModelForm):
    
    class Meta:
        model = models.Assignment
        fields = ["subject", "description", "dateDue"] 
        widgets = {
            "dateDue": forms.DateInput(attrs={"type": "date"})
        }  