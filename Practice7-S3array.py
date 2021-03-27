
a = []
n = exit
print("adad haye morede nazar ra vared konid va jahate khoroj exit benvisid")

while True:
    num = input()
    if num == n:
        break
    
    a.append(num)

b = sorted(a)

if a == b:
    print('Moratab ast')
else:
    print('Moratab Nist')