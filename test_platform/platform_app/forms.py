from django.forms import ModelForm, Textarea, TextInput,CheckboxInput
from platform_app.models import Project
from django.utils.translation import gettext_lazy as _

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['creationtime']
        widgets = {
              'name': TextInput(),
              'description': Textarea(),
         #     'status': CheckboxInput(),
        # #     'creationtime' : Textarea,
          }
        labels = {
            'name': _('Writer'),
            'description':_('description'),
        }
        help_texts = {
            'name': _('project name.'),
            'description':_('project description'),
        }