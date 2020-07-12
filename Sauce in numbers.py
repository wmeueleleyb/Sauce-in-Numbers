import requests

print('Enter a number that has 6 digits or more')
num = str(input())
codes = []
code = ''

if len(num) < 6: # If the length of the number entered is less than 6 then program tells you to try another one
    while len(num) < 6:
        print('Try another number: ', end = '')
        num = str(input())

if '.' in list(num): # This section removes any decimal points from the number
    num = list(num)
    num.remove('.')
    num = ''.join(i for i in num if i != ' ')

for i in num: # Spliting the number entered into a list where each element is a 6 digit number
    code += i
    if len(code) == 6:
        codes.append(code)
        code = ''

for i in codes: # check whether the link works using every code in the list
    url = f'https://nhentai.net/g/{i}/'
    r = requests.get(url)
    if r.status_code == 404 or len(i) != 6:
        codes.remove(i)

if len(codes) != 0:
    print('Sauce Found:\n')
    for i in codes:
        print(i)
else:
    print('No sauce was found in that number')
Exit = input()
