from django.forms import Form, ModelForm, inlineformset_factory
from django import forms
from .models import * 


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ('created_by',)

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['english_name','class_group']

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher 
        fields = ['english_name']

class SessionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.course = kwargs.pop('course', None)
        super(SessionForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Session
        fields = ['day']

# if this is used to create attendance objects, will need to get student and session of page # 
class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        exclude = ()

AttendanceFormSet = inlineformset_factory(Session, Attendance, form=AttendanceForm, extra=1)

class VocabularyForm(ModelForm):
    class Meta:
        model = Vocabulary 
        fields = ['word','definition','translation','example']

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['lesson_title','lesson_plan']

class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = ['assignment_name', 'description', 'due_date']
    

#    def __init__(self, *args, **kwargs):
#        self.fields["session_id"] = forms.CharField(widget=forms.HiddenInput())
#        super(VocabularyForm, self).__init__(self, *args, **kwargs)

#class SearchForm(Form):
#    course = forms.CharField(max_length=40, required=False)
#    search_source = forms.CHarField(max_length=20, required=False)
#    search_dest = forms.CharField(max_length=20, required=False)
 

#class StudentAttendance(Form):
#    note = forms.CharField(
#        max_length=100, widget=forms.TextInput(attrs={
#            'placeholder': 'Anything to say about this student?',
#        }),
#        required=False)

#class StudentForm(ModelForm):
#    class Meta:
#        model = Student
#        exclude = ()

#class AttendanceNoteForm(ModelForm):
#    class Meta:
#        model = AttendanceNote
#        #exclude = ('student',)
#        exclude = ()

#AttendanceNoteFormSet = inlineformset_factory(Student, AttendanceNote, form=AttendanceNoteForm, extra=1) 
#AttendanceNoteFormSet = inlineformset_factory(Attendance, AttendanceNote, form=AttendanceNoteForm, extra=1) 
