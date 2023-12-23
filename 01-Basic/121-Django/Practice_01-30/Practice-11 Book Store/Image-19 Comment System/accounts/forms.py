from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age' , )
        fields = ('username', 'age', 'email', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email', )

