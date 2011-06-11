from django import forms
from ratings.models import *

class AddForm(forms.Form):
     def __init__(self, questions, *args, **kwargs):
          super(AddForm, self).__init__(*args, **kwargs)

          for question in questions:
               key = "question%d" % question.id
               if question.hasRate:
                    CHOICES = []
                    for i in range(1, Response.rateMax + 1):
                         CHOICES.append((i,i))
                    self.fields[key] = forms.ChoiceField(initial=Response.rateMax / 2, choices=CHOICES)
               else:
                    self.fields[key] = forms.CharField()
               self.fields[key].label = question.question;
