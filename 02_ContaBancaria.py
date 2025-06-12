## V1.0 Desafio 02 - Conta Bancaria
## Autor: EvertonCaFer
## 12-06-2025
import textwrap;
from datetime import datetime, date;

#### Dados do Banco ###
## Dados Usuario ##
lista_usuarios = [];
usuario_logado = None;

## Dados Conta ##
AGENCIA = "0001";
lista_contas = [];
conta = None;
saldo = 0;
extrato = "";
limite = 500;
numero_saques = 0;
LIMITE_SAQUES = 3;

## Dados Exras ##
data_hoje = datetime.today();


def login():
    opcao = """
    === BEM VINDO AO BANCO DE NARNIA ===

    [1] Entrar na conta.
    [2] Cadastrar novo usuário.
    [3] Carregar dados para teste.
    [q] Sair

    => """
    return input(textwrap.dedent(opcao).strip().lower());

def menu():
    menu = """
    =============== MENU PRINCIPAL ===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [lc]Listar contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu).strip().lower());

def depositar (valor, saldo, extrato, /): # A barra representa a passagem por posição
    if valor > 0:
        saldo += valor;
        extrato += f"Depósito de R${valor:.2f}\n";
        print(f"Depósito de R${valor} realizado com sucesso!");

    else:
        print("Valor incorreto para depósito!");

    return saldo, extrato;
    
def sacar (*, valor, saldo, extrato, limite, numero_saques, limite_saques):
    if (valor < saldo) and (valor <= limite) and (numero_saques >= 0 ) and (numero_saques < LIMITE_SAQUES):
        saldo -= valor;
        extrato += f"Saque de R${valor:.2f}\n";
        numero_saques += 1;
        print(f"Saque de R${valor} realizado com sucesso!");

    elif numero_saques >= LIMITE_SAQUES:
        print(f"Operação falhou! Limite de {LIMITE_SAQUES} saques utilizados no dia!");
    
    elif valor > limite:
        print(f"Operação falhou! Valor do saque excede o limite!");

    else:
        print(f"Operação falhou! Você não possui saldo suficiente!");

    return saldo, extrato, numero_saques;

def exibir_extrato (saldo, /, *, extrato):
    print("\n ========= Extrato =========");
    print("Não foram realizadas movimentações." if not extrato else extrato);
    print(f"\nSaldo R${saldo:.2f}");
    print("==============================");

def criar_usuario(lista_usuarios):
    cpf = input("Digite o CPF (Somente numeros): ");
    usuario = filtrar_usuario(cpf, lista_usuarios);

    if usuario: print("Usuario já cadastrado com este CPF."); return; #True se o usuario já existe

    nome = input("Nome: ");
    data_nascimento = input("Data de Nascimento (dd-mm-aaaa): ");
    endereco = input("Endereço (Logradouro, Nº - Bairro - Cidade/Estado): ");

    lista_usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuario Criado Com Sucesso!");

def filtrar_usuario(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario_logado):
    print("\n=== Conta criada com sucesso! ===")
    return {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_logado
    }

def listar_contas(lista_contas):
    for conta in lista_contas:
        linha = f"""\n\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

def carregar_dados_teste(lista_usuarios, contas):
    numero_conta = len(lista_contas)+1;
    usuario = {
        "nome": "Maria Teste",
        "data_nascimento": "10-06-1990",
        "cpf": "11122233344",
        "endereco": "Rua Fictícia, 123 - Bairro - Cidade/UF"
    }
    lista_usuarios.append(usuario)
    conta = criar_conta("0001", numero_conta, usuario)
    contas.append(conta)
    print("\n=== Dados de teste carregados com sucesso! ===")
    return usuario


while True:
    opcao = login();

    if opcao == "1":
            cpf = input("Informe seu CPF: ")
            usuario = filtrar_usuario(cpf, lista_usuarios)
            if usuario:
                usuario_logado = usuario
                print(f"\nBem-vindo, {usuario_logado['nome']}!")
            
                while True: ### OPCOES DA CONTA ###
                    opcao = menu();

                    if opcao == "d": ### DEPOSITO ###
                        print("=== Depósito ===");
                        valor = float(input("insira o valor a ser depositado: "));
                        saldo, extrato = depositar(valor, saldo, extrato, );

                    elif opcao == "s": ### SAQUE ###
                        print(" === Saque ===");
                        valor = float(input("Informe o valor a ser sacado: "));
                        saldo, extrato, numero_saques = sacar(
                            valor = valor, 
                            saldo = saldo, 
                            extrato = extrato,
                            limite = limite,
                            numero_saques = numero_saques,
                            limite_saques = LIMITE_SAQUES);

                    elif opcao == "e": ### EXTRATO ###
                        exibir_extrato(saldo, extrato = extrato);

                    elif opcao == "c": ### CRIAR CONTA ###
                        numero_conta = len(lista_contas) + 1;
                        nova_conta = criar_conta(AGENCIA, numero_conta, usuario_logado);
                        
                        if nova_conta:
                            lista_contas.append(nova_conta);

                    elif opcao == "lc": ### LISTAR CONTAS ###
                        listar_contas(lista_contas);
                    
                    elif opcao == "q": ### SAIR ###
                        break;

                    else:
                        print("Operação inválida, por favor selecione novamente a operação desejada.");

            else:
                print("\nCPF não encontrado,  favor se cadastrar primeiro!");

    elif opcao == "2":
        criar_usuario(lista_usuarios);

    elif opcao == "3":
        usuario_logado = carregar_dados_teste(lista_usuarios, lista_contas);

    elif opcao == "q":
        print("Encerrando o sistema.");
        break;

    else:
        print("Opção inválida. Tente novamente.")





        

