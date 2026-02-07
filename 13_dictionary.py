dict = {
    'kaam':'work',
    'kitab':'book',
    'chalna':'walk'
}
print(dict['chalna'])
print(dict.get('kitab'))

print('on get : ',dict.get('kudna')) #none
# print('on index: ',dict['kudna']) #error

print(dict.items())
print(dict.keys())
dict.update({'kudna':'jump',
              'chalna':'walk',
              0:'run'})
print(dict)

newd = {
    'hi':1,
    'hi':2
}
print(newd)