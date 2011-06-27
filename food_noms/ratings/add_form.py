from django import forms
from ratings.models import *

class AddForm(forms.Form):
     def __init__(self, questions, *args, **kwargs):
          super(AddForm, self).__init__(*args, **kwargs)

          for question in questions:
               key = "%d" % question.id
               if question.type == Question.QUESTION_TYPE_RATING:
                    CHOICES = []
                    for i in range(1, RatingResponse.RESPONSE_MAX_RATING + 1):
                         CHOICES.append((i,i))
                    self.fields[key] = forms.ChoiceField(initial=RatingResponse.RESPONSE_MAX_RATING / 2, choices=CHOICES)
               if question.type == Question.QUESTION_TYPE_FREE_RESPONSE:
                    self.fields[key] = forms.CharField()
               self.fields[key].label = question.question;
