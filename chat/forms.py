from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'username', 'email', 'password1', 'password2']
        
        def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)
             self.helper = FormHelper()
             self.helper.form_id = 'id-exampleForm'
             self.helper.form_class = 'blueForms'
             self.helper.form_method = 'post'
             self.helper.form_action = 'submit_survey'

             self.helper.add_input(Submit('submit', 'Submit'))
             



