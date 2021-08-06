num = (int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")))
if num == 9:
    print(f"O numero 9 apareceu {num.count(9)} vezes")
print(f"A posilçai do numero 3 é: {num.index(3)}")
print("Os Numeros pares são: ", end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
