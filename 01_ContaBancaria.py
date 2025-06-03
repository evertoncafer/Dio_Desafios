## v1.0 Desafio Conta Bancaria
## Autor: EvertonCaFer
## 02-05-2025

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0;
limite = 500;
extrato = "";
numero_saques = 0;
LIMITE_SAQUES = 3;

while True:

    opcao = input(menu);

    if opcao == "d":
        print("=== Depósito ===");
        valor = float(input("insira o valor a ser depositado: "));
        
        if valor > 0:
            saldo += valor;
            extrato += f"Depósito de R${valor:.2f}\n";
            print(f"Depósito de R${valor} realizado com sucesso!");


        else:
            print("Valor incorreto para depósito!");

    elif opcao == "s":
        print(" === Saque ===");
        valor = float(input("Informe o valor a ser sacado: "));
    
        if (valor < saldo) and (valor <= limite) and (numero_saques >= 0 ) and (numero_saques < LIMITE_SAQUES):
            saldo -= valor;
            extrato += f"Saque de R${valor:.2f}\n";
            numero_saques += 1;
            print(f"Saque de R${valor} realizado com sucesso!");

        elif numero_saques >= 3:
            print(f"Operação falhou! Limite de {LIMITE_SAQUES} saques utilizados no dia!");
        
        elif valor > limite:
            print(f"Operação falhou! Valor do saque excede o limite!");

        else:
            print(f"Operação falhou! Você não possui saldo suficiente!");

    elif opcao == "e":
        print("\n ========= Extrato =========");
        print("Não foram realizadas movimentações." if not extrato else extrato);
        print(f"\nSaldo R${saldo:.2f}");
        print("==============================");

    elif opcao == "q":
        break;

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.");

