from django import forms
from .models import Reservations
from .models import Contact


class ReservationsForm(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(
                                    attrs={'type': 'text', 'name': 'name', 'id': 'name', 'class': 'form-control',
                                           'placeholder': 'Имя', 'required': 'required',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'name': 'email', 'class': 'form-control',
                                      'placeholder': 'Email', 'required': 'required', 'data-rule': 'email',
                                      'data-msg': 'Please enter a valid email'}))

    user_phone = forms.CharField(max_length=15,
                                 widget=forms.TextInput(
                                     attrs={'type': 'text', 'name': 'phone', 'id': 'phone', 'class': 'form-control',
                                            'placeholder': 'Телефон', 'required': 'required',
                                            'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    user_date = forms.CharField(max_length=15,
                                widget=forms.TextInput(
                                    attrs={'type': 'text', 'name': 'date', 'id': 'date', 'class': 'form-control',
                                           'placeholder': 'Date', 'required': 'required',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    user_time = forms.CharField(max_length=15,
                                widget=forms.TextInput(
                                    attrs={'type': 'text', 'name': 'time', 'id': 'time', 'class': 'form-control',
                                           'placeholder': 'time', 'required': 'required',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    number_of_person = forms.CharField(max_length=15,
                                       widget=forms.TextInput(
                                           attrs={'type': 'number', 'name': 'people', 'id': 'people',
                                                  'class': 'form-control',
                                                  'placeholder': '# of people', 'required': 'required',
                                                  'data-rule': 'minlen:1',
                                                  'data-msg': 'Please enter at least 1 chars'}))

    user_message = forms.CharField(max_length=400,
                                   widget=forms.Textarea(
                                       attrs={'type': 'message', 'name': 'message', 'class': 'form-control',
                                              'rows': '5', 'placeholder': 'Сообщение', 'required': 'required'}))

    class Meta:
        model = Reservations
        fields = ('user_name', 'user_email', 'user_phone', 'user_date', 'user_time', 'number_of_person', 'user_message')


class ContactForm(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(
                                    attrs={'type': 'text', 'name': 'name', 'id': 'name', 'class': 'form-control',
                                           'placeholder': 'Your Name', 'required': 'required',}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'name': 'email', 'class': 'form-control',
                                      'placeholder': 'Your Email', 'required': 'required'}))

    user_subject = forms.CharField(max_length=40,
                                   widget=forms.TextInput(
                                       attrs={'type': 'text', 'name': 'subject', 'id': 'subject',
                                              'class': 'form-control', 'placeholder': 'Subject',
                                              'required': 'required'}))

    user_message = forms.CharField(max_length=400,
                                   widget=forms.Textarea(
                                       attrs={'name': 'message', 'class': 'form-control',
                                              'rows': '5', 'placeholder': 'Message', 'required': 'required'}))

    class Meta:
        model = Contact
        fields = ('user_name', 'user_email', 'user_subject', 'user_message')
