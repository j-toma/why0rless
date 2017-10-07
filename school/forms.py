from django.forms import ModelForm, inlineformset_factory
from .models import Student, Attendance, AttendanceNote


class AttendanceForm(ModelForm):
#    attended = forms.BooleanField(
#        label='Attended',
#        required=True,
#        initial=False
#    )
    class Meta:
        model = Attendance
        fields = ['attended','was_late']

#AttendanceFormSet = inlineformset_factory(Session, Student, form=AttendanceForm, extra=1)

#class StudentAttendance(Form):
#    note = forms.CharField(
#        max_length=100, widget=forms.TextInput(attrs={
#            'placeholder': 'Anything to say about this student?',
#        }),
#        required=False)

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ()

class AttendanceNoteForm(ModelForm):
    class Meta:
        model = AttendanceNote
        #exclude = ('student',)
        exclude = ()

#AttendanceNoteFormSet = inlineformset_factory(Student, AttendanceNote, form=AttendanceNoteForm, extra=1) 
AttendanceNoteFormSet = inlineformset_factory(Attendance, AttendanceNote, form=AttendanceNoteForm, extra=1) 
