from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
    widget = forms.TextInput(
        attrs={'class':'form-control','placeholder' :'Enter todo e.g for grocery shopping',
        'aria-label':'Todo','aria-describeby':'add-btn'}
    ))

    #<input type="text" class="form-control" placeholder="Enter todo e.g grocery shopping" aria-label="Todo" aria-describedby='add-btn'>