from django.forms import ModelForm
from .models import Task, Project
from django.core.exceptions import ValidationError

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'project', 'due_date', 'tags']

    def clean_title(self):
        title = self.cleaned_data['title']

        if "test" in title.lower():
            raise ValidationError("Tytuł nie może zawierać słowa 'test'.")
        return title.capitalize()

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
