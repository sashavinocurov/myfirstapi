import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxNzg4OTQwLCJqdGkiOiIxZDdiOWQwNzIwMjk0NTAxYjQwYzBlZGFhNDkwZmQzMCIsInVzZXJfaWQiOjF9.Q_GXOAi4ZHBDQtuB_kJfpU8ELp__9grr3mYSIoNmO2M'

r = requests.get('http://localhost:8000/paradigms/', headers=headers)

print(r.text)