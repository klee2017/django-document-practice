# Model field reference
## null

참이면, Django는 데이터베이스에 빈 값을 NULL로 저장할 것이다. 기본 값은 False.

CharField나 TextField와 같은 string-based field에서 null을 사용하는 것을 피하자. If a string-based field has null=True, that means it has two possible values for “no data”: NULL, and the empty string. In most cases, it’s redundant to have two possible values for “no data;” the Django convention is to use the empty string, not NULL. One exception is when a CharField has both unique=True and blank=True set. In this situation, null=True is required to avoid unique constraint violations when saving multiple objects with blank values.

For both string-based and non-string-based fields, you will also need to set blank=True if you wish to permit empty values in forms, as the null parameter only affects database storage (see blank).

If you want to accept null values with BooleanField, use NullBooleanField instead.

## blank

If True, the field is allowed to be blank. Default is False.

Note that this is different than null. null is purely database-related, whereas blank is validation-related. If a field has blank=True, form validation will allow entry of an empty value. If a field has blank=False, the field will be required.

##choices

An iterable (e.g., a list or tuple) consisting itself of iterables of exactly two items (e.g. [(A, B), (A, B) ...]) to use as choices for this field. If this is given, the default form widget will be a select box with these choices instead of the standard text field.

The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name.

Generally, it’s best to define choices inside a model class, and to define a suitably-named constant for each value.

Though you can define a choices list outside of a model class and then refer to it, defining the choices and names for each choice inside the model class keeps all of that information with the class that uses it, and makes the choices easy to reference (e.g, Student.SOPHOMORE will work anywhere that the Student model has been imported).

You can also collect your available choices into named groups that can be used for organizational purposes.

The first element in each tuple is the name to apply to the group. The second element is an iterable of 2-tuples, with each 2-tuple containing a value and a human-readable name for an option. Grouped options may be combined with ungrouped options within a single list (such as the unknown option in this example).

For each model field that has choices set, Django will add a method to retrieve the human-readable name for the field’s current value. See get_FOO_display() in the database API documentation.

Note that choices can be any iterable object – not necessarily a list or tuple. This lets you construct choices dynamically. But if you find yourself hacking choices to be dynamic, you’re probably better off using a proper database table with a ForeignKey. choices is meant for static data that doesn’t change much, if ever.

Unless blank=False is set on the field along with a default then a label containing "---------" will be rendered with the select box. To override this behavior, add a tuple to choices containing None; e.g. (None, 'Your String For Display'). Alternatively, you can use an empty string instead of None where this makes sense - such as on a CharField.

## db_column

The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.

If your database column name is an SQL reserved word, or contains characters that aren’t allowed in Python variable names – notably, the hyphen – that’s OK. Django quotes column and table names behind the scenes.

## db_index

If True, a database index will be created for this field.

## db_tablespace

The name of the database tablespace to use for this field’s index, if this field is indexed. The default is the project’s DEFAULT_INDEX_TABLESPACE setting, if set, or the db_tablespace of the model, if any. If the backend doesn’t support tablespaces for indexes, this option is ignored.

## default

The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created.

The default can’t be a mutable object (model instance, list, set, etc.), as a reference to the same instance of that object would be used as the default value in all new model instances. Instead, wrap the desired default in a callable.

lambdas can’t be used for field options like default because they can’t be serialized by migrations. See that documentation for other caveats.

For fields like ForeignKey that map to model instances, defaults should be the value of the field they reference (pk unless to_field is set) instead of model instances.

The default value is used when new model instances are created and a value isn’t provided for the field. When the field is a primary key, the default is also used when the field is set to None.

## editable

If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True.

## error_message

The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override.

Error message keys include null, blank, invalid, invalid_choice, unique, and unique_for_date. Additional error message keys are specified for each field in the Field types section below.

These error messages often don’t propagate to forms. See Considerations regarding model’s error_messages.

## help_text

Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.

Note that this value is not HTML-escaped in automatically-generated forms. This lets you include HTML in help_text if you so desire.

Alternatively you can use plain text and django.utils.html.escape() to escape any HTML special characters. Ensure that you escape any help text that may come from untrusted users to avoid a cross-site scripting attack.

## primary_key

If True, this field is the primary key for the model.

If you don’t specify primary_key=True for any field in your model, Django will automatically add an AutoField to hold the primary key, so you don’t need to set primary_key=True on any of your fields unless you want to override the default primary-key behavior. For more, see Automatic primary key fields.

primary_key=True implies null=False and unique=True. Only one primary key is allowed on an object.

The primary key field is read-only. If you change the value of the primary key on an existing object and then save it, a new object will be created alongside the old one.

## unique

출처: https://docs.djangoproject.com/en/1.11/ref/models/fields/