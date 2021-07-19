from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(error_messages={
        'required': 'Please enter subject'
    }, label='subject', max_length=100)
    message = forms.CharField(error_messages={
        'required': 'Please enter message'
    }, label='message', widget=forms.Textarea)
    sender = forms.EmailField(error_messages={
        'required': 'Please check sender email id'
    }, label='sender')
    cc_myself = forms.BooleanField(required=False)


# here are other output options though for the <label>/<input> pairs: in the template

# {{form.as_table}} will render them as table cells wrapped in <tr > tags
# {{form.as_p}} will render them wrapped in <p > tags
# {{form.as_ul}} will render them wrapped in <li > tags
