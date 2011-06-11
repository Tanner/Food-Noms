from django import forms

class AddForm(forms.Form):
     def __init__(self, questions, *args, **kwargs):
          super(AddForm, self).__init__(*args, **kwargs)

          for question in questions:
               key = "question%d" % question.id
               if question.hasRate:
                    self.fields[key] = forms.ChoiceField()
               else:
                    self.fields[key] = forms.CharField()
               self.fields[key].label = question.question;
