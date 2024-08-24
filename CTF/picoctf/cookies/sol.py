import requests
for i in range(25):
    cookie = 'name={}'.format(i)
    headers = {'Cookie':cookie}
    
    r = requests.get('http://mercury.picoctf.net:6418//check', headers=headers)
    print(r.text)

# To run do:
# python3 sol.py | gre picoCTF{
