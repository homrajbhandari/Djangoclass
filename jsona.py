import json
json_string ='''
{
    "id":1,
    "title":"The great sky"}
    '''
    

book=json.loads(json_string)
print(book['title'])
