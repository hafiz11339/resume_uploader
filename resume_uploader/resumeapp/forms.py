from django import forms
from .models import Resume
GENDER_CHOICES = [
    ("Male","Male"),
    ("Female","Female")
]


JOB_CITY =(
    ("Lhr","Lhr"),
    ("Karachi","Karachi")
)

class ResumeForm(forms.ModelForm):
    # gender = forms.ChoiceField(choices=GENDER_CHOICES) # this is select for radio code is below
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    # The below is checkbox code
    # job_city = forms.MultipleChoiceField(label='Job Locations',choices=JOB_CITY,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = '__all__'
        # labels lowercase
        labels = {'dob':"Date Of Birth",'pin':'Pin Code',"mobile":"Mobile Number"}

        widgets = {
            "name":forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


