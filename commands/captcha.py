import random


words = "abcdefghijklmnopqrstuvwxyz0123456789"

captcha = ''.join((random.choice(words) for i in range(6)))
print(captcha)

v = input("Informe o captcha: ")
new_v = v.lower()

print(captcha)
print(new_v)

if captcha == new_v:
    print("OK")
else:
    print("Não OK!")
