from django import forms
import numpy as np

class DataForm(forms.Form):
    distance_from_home = forms.FloatField(label='Distance From Home', required=True)
    distance_from_last_transaction = forms.FloatField(label='Distance From Last Transaction', required=True)
    ratio_to_median_purchase_price = forms.FloatField(label='Ratio to Median Purchase Price', required=True)
    repeat_retailer = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')], label='Repeat Retailer', required=True)
    used_chip = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')], label='Used Chip', required=True)
    used_pin_number = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')], label='Used Pin Number', required=True)
    online_order = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')], label='Online Order', required=True)


    def to_np(self):
        data = [[
            self.cleaned_data['distance_from_home'],
            self.cleaned_data['distance_from_last_transaction'],
            self.cleaned_data['ratio_to_median_purchase_price'],
            self.cleaned_data['repeat_retailer'],
            self.cleaned_data['used_chip'],
            self.cleaned_data['used_pin_number'],
            self.cleaned_data['online_order'],
            0
        ]]
       
        return np.array(data, dtype="float32")
       

        
    

   

