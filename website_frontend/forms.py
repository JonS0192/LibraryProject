from django import forms


class AddBookForm(forms.Form):
    isbn = forms.CharField(label='ISBN')
    title = forms.CharField(label='Title')
    author = forms.CharField(label='Author')


class UpdateBookForm(forms.Form):
    isbn = forms.CharField(label='ISBN')
    title = forms.CharField(label='Title')
    author = forms.CharField(label='Author')


class GetBookForm(forms.Form):
    input_type = forms.CharField(label='Input Type')
    input = forms.CharField(label='Input')


class DeleteBookForm(forms.Form):
    isbn = forms.CharField(label='ISBN')


class AddLibraryCardForm(forms.Form):
    id = forms.CharField(label='ID')
    name = forms.CharField(label='Name')
    phone_number = forms.CharField(label='Phone Number')
    email = forms.CharField(label='Email')


class GetLibraryCardForm(forms.Form):
    input_type = forms.CharField(label='Input Type')
    input = forms.CharField(label='Input')


class UpdateLibraryCardForm(forms.Form):
    id = forms.CharField(label='ID')
    name = forms.CharField(label='Name')
    phone_number = forms.CharField(label='Phone Number')
    email = forms.CharField(label='Email')


class DeleteLibraryCardForm(forms.Form):
    id = forms.CharField(label='ID')


class AddCheckedOutForm(forms.Form):
    id = forms.CharField(label='ID')
    isbn = forms.CharField(label='ISBN')


class DeleteCheckedOutForm(forms.Form):
    isbn = forms.CharField(label='ISBN')