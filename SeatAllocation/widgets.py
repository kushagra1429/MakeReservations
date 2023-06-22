# from datetime import date
# from django import forms

# class NewDatePicker(forms.DateInput):
#     DATE_INPUT_FORMAT='%Y-%m-%d'
#     def __init__(self, attrs={}, format=None):
#         attrs.update(
#             {
#                 'class': 'form-control',
#                 'type':'date',
#             }
#         )
#         self.format=self.DATE_INPUT_FORMAT
#         super().__init__(attrs, format=self.format)