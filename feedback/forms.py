import floppyforms as forms

from core.models import McUser
from models import Applicant, Feedback, State, Event, InterviewerFeedback

class ImageThumbnailInput(forms.ClearableFileInput):
  template_name = 'floppyforms/image_thumbnail.html'

class RadioNoULInput(forms.RadioSelect):
  template_name = 'floppyforms/radio_no_ul.html'
  
class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields =[
      'full_name',
      'name',
      'fw',
      'survey_link'
    ]

class ApplicantForm(forms.ModelForm):
  class Meta:
    model = Applicant
    fields = [
        'first_name',
        'last_name',
        'gender',
        'hometown',
        'hometown_state',
        'high_school',
        'pic',
        'actual_pic',
        'attended',
        'major',
        'career',
        'group',
    ]
    widgets = {
        'pic': ImageThumbnailInput,
        'actual_pic': ImageThumbnailInput,
    }

class FeedbackForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(FeedbackForm, self).__init__(*args, **kwargs)

    #strip out the '---------' option that is inserted b/c blank=True in the models
    self.fields['rating'].choices = self.fields['rating'].choices[1:]
    self.fields['interest'].choices = self.fields['interest'].choices[1:]

  class Meta:
    model = Feedback
    fields = [
      'rating',
      'interest',
      'comments',
      'notes',
    ]
    widgets = {
      'rating': RadioNoULInput,
      'interest': RadioNoULInput,
      'comments': forms.Textarea(attrs={'rows':4}),
      'notes': forms.Textarea(attrs={'rows':4}),
    }

class InterviewerFeedbackForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(InterviewerFeedbackForm, self).__init__(*args, **kwargs)

    #strip out the '---------' option that is inserted b/c blank=True in the models
    self.fields['rating'].choices = self.fields['rating'].choices[1:]

  class Meta:
    model = InterviewerFeedback
    fields = [
      'checkbox_1',
      'checkbox_2',
      'checkbox_3',
      'checkbox_4',
      'checkbox_5',
      'checkbox_6',
      'checkbox_7',
      'checkbox_8',
      'checkbox_9',
      'checkbox_10' ,
      'checkbox_11',
      'checkbox_12',
      'checkbox_13',
      'checkbox_14',
      'checkbox_15' ,
      'checkbox_16',
      'checkbox_17',
      'checkbox_18',
      'question_1',
      'question_2',
      'question_3',
      'question_4',
      'question_5',
      'question_6',
      'rating',
      'comments',
    ]
    widgets = {
      'rating': RadioNoULInput,
      'question_1': forms.Textarea(attrs={'rows':4}),
      'question_2': forms.Textarea(attrs={'rows':4}),
      'question_3': forms.Textarea(attrs={'rows':4}),
      'question_4': forms.Textarea(attrs={'rows':4}),
      'question_5': forms.Textarea(attrs={'rows':4}),
      'question_6': forms.Textarea(attrs={'rows':4}),
      'comments': forms.Textarea(attrs={'rows':4}),
    }

class StateForm(forms.ModelForm):
  class Meta:
    model = State
    fields = [
      'current'
    ]
    widgets = {
      'current': RadioNoULInput
    }