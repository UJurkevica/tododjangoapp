from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g Grocerry shopping', 'arial-label' : 'Todo', 'aria-describeby' : 'add-btn'}))
