import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxNzkyMTU2LCJqdGkiOiI1MGNmY2QwYzcwYTU0M2E1OTk3OWM3YzkzODk4MjRkMiIsInVzZXJfaWQiOjF9.xwlgJP9wdM3DeLtPBjFktaYGE_t5iKez8Auob52wFZo'

r = requests.get('http://localhost:8000/programmers/', headers=headers)

print(r.text)