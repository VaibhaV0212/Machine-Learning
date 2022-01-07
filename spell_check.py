from gingerit.gingerit import GingerIt

# text = input('Enter string= ')
# text = 'i lv u'

text = 'i hv a startup code to use gingerit on pthon. Gingerit is by far the mst enhanced and they best gramar tol avalable on python. when i try running the code I have, I started receiving a traceback error. i m currently using 3.7 nd te code i used is present on the official gingerit documentation.'
print('Length is = ',len(text.split()))
parser = GingerIt()
print('Original text is = ',parser.parse(text)['text'])
# print(parser.parse(text)['corrections'][0]['start'])
print('Correct sentence is = ',parser.parse(text)['result'])
# count_worng = parser.parse(text)['result']