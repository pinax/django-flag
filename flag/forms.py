from django.contrib.auth.models import User
from django import forms
from django.contrib.contenttypes.models import ContentType

class FlagForm(forms.ModelForm):
    """
    Form for submitting a flagged content object and comment
    """

    comment = forms.CharField(
        label = 'comment',
        widget = forms.Textarea
    )

    class Meta:
        models = FlagInstance
        fields = ('comment')
