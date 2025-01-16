while True:
    print('---------------------')
    print('(|---Calculadora---|)')
    print('(|ADIÇÃO-(1)-------|)')
    print('(|SUBTRAÇÃO-(2)----|)')
    print('(|MULTIPLICAÇÃO-(3)|)')
    print('(|DIVISÃO-(4)------|)')
    print('(|SAIR-(5)---------|)')
    print('---------------------')
    op=input('Escolha uma opção =>')

    if op=="5":
        print("ENCERRANDO...")
        print('|----------------------|')
        print("|--PROGRAMA ENCERRADO--|")
        print('|----------------------|')
        break

    if op=="1":
        print("(|--ADIÇÃO--|)")
        n1=int(input('Digite um numero:'))
        n2=int(input('Digite outro numero:'))
        soma=n1+n2
        print(f'{n1}+{n2}={soma}')
        
    if op=="2":
        print('(|--SUBTRAÇÃO--|)')
        n3=int(input('Digite um numero:'))
        n4=int(input('Digite outro numero:'))
        sub=n3-n4
        print(f'{n3}-{n4}={sub}')  
       
    if op=="3":
        print('(|--MULTIPLICAÇÃO--|)')
        n5=int(input('Digite um numero:'))
        n6=int(input('Digite outro numero:'))
        multi=n5*n6
        print(f'{n5}x{n6}={multi}')
        
    if op=="4":
        print('(|--DIVISÃO--|)')
        n7=int(input('Digite um numero:'))
        n8=int(input('Digite outro numero:'))
        div=n7/n8
        print(f'{n7}/{n8}={div}')