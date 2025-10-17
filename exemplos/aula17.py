num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7    # Não é possível como em PHP
# num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
print(num)
num.pop(4)
print(num)
if 7 in num:
    num.remove(7)
else:
    print(f'Não achei o número 7')
print(num)
print(f'Esta lista tem {len(num)} elementos')
