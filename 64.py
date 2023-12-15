import base64

s = '''
SGVsbG8gd29ybGQgISBHbyB0byBiZWQh
'''
print(base64.b64decode(s).decode())

#Расшифровываем base64