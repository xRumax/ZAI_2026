from django.forms import ModelForm
from .models import Task, Project
from django.core.exceptions import ValidationError
import datetime
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'project', 'due_date', 'tags']

    def clean_title(self):
        title = self.cleaned_data['title']

        if "test" in title.lower():
            raise ValidationError("Tytuł nie może zawierać słowa 'test'.")
        return title.capitalize()
    
    def clean_due_date(self):
        date_now = datetime.date.today()
        due_date = self.cleaned_data.get('due_date')
        if due_date < date_now:
            raise ValidationError("Data nie może być w przeszłości")
        return due_date
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
