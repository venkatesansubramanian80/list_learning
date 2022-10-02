dict_values = {'manual_color': 'yellow', 'approved_color': 'green', 'rejected_color': 'red'}
print(dict_values)
print(dict_values.get('approved_color'))
dict_values['manual_color'] = 'black'
print(dict_values.get('manual_color'))