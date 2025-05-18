# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# # from django import forms
# # from .models import Order



# from django import forms
# from .models import Order

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['name', 'email', 'phone', 'address', 'payment_method', 'upi_id', 'ordered_items']


#         widgets = {
#             'items': forms.CheckboxSelectMultiple()
#         }

# from django import forms
# from .models import Order

# class OrderForm(forms.ModelForm):
#     payment_method = forms.ChoiceField(choices=[
#         ('Cash on Delivery', 'Cash on Delivery'),
#         ('UPI', 'UPI'),
#         ('Card', 'Credit/Debit Card'),
#     ])
#     upi_id = forms.CharField(required=False)
#     ordered_items = forms.CharField(widget=forms.HiddenInput(), required=False)

#     class Meta:
#         model = Order
#         fields = ['customer_name', 'phone', 'email', 'address', 'payment_method', 'upi_id', 'ordered_items']
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order

# User Signup Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Order Placement Form
class OrderForm(forms.ModelForm):
    payment_method = forms.ChoiceField(choices=[
        ('Cash on Delivery', 'Cash on Delivery'),
        ('UPI', 'UPI'),
        ('Card', 'Credit/Debit Card'),
    ])
    upi_id = forms.CharField(required=False)
    ordered_items = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'email', 'address', 'payment_method', 'upi_id', 'ordered_items']
