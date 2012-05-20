#####
Forms
#####

* Overwrite only the widget of a modelform

.. code-block:: python 

  class MyForm2(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         super(MyForm2, self).__init__(*args, **kwargs)
         self.fields['myfield1'].required = True
         self.fields[‘myfield1’].widget = forms.Textarea(attrs {‘class’:’myclass’,})
     class Meta:
         model = models.MyModel

* Custom error message

.. code-block:: python 

  class MyForm2(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         super(MyForm2, self).__init__(*args, **kwargs)
         self.fields['rating'].error_messages['required'] = 'I require that you fill out this field'

* Custom validator

.. code-block:: python 

  def clean_myfield(self):
    if self.cleaned_data["myfield"] < 10:
      raise forms.ValidationError("MyField must be greater than 10")

    return self.cleaned_data["myfield"]

* Loop over all form fields

.. code-block:: python 

  {% for field in form %}
    {{ field.label_tag }} {{ field }}
  {% endfor %}

* Display form value without None

.. code-block:: python 
 
 {{ form.field.value|default_if_none:"" }}

* Request if a field is required

.. code-block:: python 

  {% if form.field_name.field.required %}

* Display error without li-tags

.. code-block:: python 

  {{ field.errors|striptags }} 

* Create Form from Model with https://github.com/bradleyayers/django-tables2/
