from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nombre', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.password = self.cleaned_data['password']
        if commit:
            usuario.save()
        return usuario
    
class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'email')