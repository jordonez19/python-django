from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="title",max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="description")

class CreateNewProject(forms.Form):
    name = forms.CharField(label="name",max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="description")
