from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields
        fields = ('username', 'email', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', )
        # fields = UserCreationForm.Meta.fields



