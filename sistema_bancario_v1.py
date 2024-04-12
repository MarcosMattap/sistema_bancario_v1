#Esta é a versão 1 do desafio de sistema bancário

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
  
   # Opção de depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            
            saldo += valor

            extrato += f"depósito: R$ {valor:.2f}\n"
        
        else:
            print("Falha na operação! O valor informado não é válido.")
    
    
    # Opção de saque
    elif opcao == "s":
        
        valor = float(input("Informe o valor do saque: "))
        
        sem_saldo = valor > saldo
        
        sem_limite = valor > limite
        
        saque_indisponivel = numero_saques >= LIMITE_SAQUES
        
        if sem_saldo:
            print("Saldo insuficiente. falha na operação!")
        
        elif sem_limite:
            print("O valor solicitado é maior que o valor permitido.")
        
        elif saque_indisponivel:
            print("Número de saques exedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
    
    # Opção de extato
    elif opcao == "e":
       print("\n================ EXTRATO ================")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("=========================================")
    
    
    # Opção de saida 
    elif opcao == "q":
        break
    else:
     print("Operação invalida, por favor selecione novamente a opção desejada.")

     # Desenvolvido por Marcos Pereira.