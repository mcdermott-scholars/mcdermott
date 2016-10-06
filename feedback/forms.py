import floppyforms as forms

from core.models import McUser
from models import Applicant, Feedback, State, Event

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

class StateForm(forms.ModelForm):
  class Meta:
    model = State
    fields = [
      'current'
    ]
    widgets = {
      'current': RadioNoULInput
    }