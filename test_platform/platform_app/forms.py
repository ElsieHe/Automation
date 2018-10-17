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
              'status': CheckboxInput(),
        # #     'creationtime' : Textarea,
          }
        labels = {
            'name': _('名称'),
            'description':_('描述'),
            'status':_('状态'),
        }
        help_texts = {
            'name': _('***项目名称'),
            'description':_('***项目说明'),
        }
        error_messages = {
            '__all__': {

            },
            'name': {
                'required': '项目不能为空',
            },
            'description':{
                'required':'说明不能为空',
            }
        }