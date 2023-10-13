from PilhaSequencial import Pilha, PilhaException

p = Pilha()
pilsel = 1
numdisp = [1]
while True:
    try:
        print(f'''
Editor de Pilha v1.2
=====================================
Pilha Selecionada: {pilsel} de 10
{p}
=====================================
(e) Empilhar
(d) Desempilhar
(t) Tamanho
(o) Obter elemento do topo
(v) Teste de pilha vazia
(r) Criar nova Pilha
(j) Inverter os elementos da pilha
(z) Esvaziar a pilha
(c) Concatenar duas pilhas
(m) Escolher outra pilha
(n) Conversão dec/bin
(s) Sair
=====================================''')
        resposta = input("Digite sua opção: ").lower()
        if (resposta == "e"):
            valor = input("Digite o valor que será empilhado: ")
            p.empilha(valor)
        elif (resposta == "d"):
            print(p.desempilha())
        elif (resposta == "t"):
            print(len(p))
        elif (resposta == "o"):
            print(p.topo())
        elif (resposta == "v"):
            print(p.estaVazia())
        elif (resposta == "r"):
            if (len(numdisp) != 10):
                tam = int(input("Qual o tamanho da pilha? "))
                if (tam < 1):
                    raise PilhaException("Tamanho inválido.")
                else:
                    numdisp.append(numdisp[-1] + 1)
                    print(p.criarPilha(numdisp[-1], tam))
                    print(f"O número da sua nova pilha é {numdisp[-1]}, deseja seleciona-la? (S) ou (N)")
                    sel = input("Opção: ").upper()
                    if (sel == "S"):
                        pilsel = numdisp[-1]
                        print(p.escolherPilha(pilsel))
                    else:
                        print("Pilha atual: ")
            else:
                raise PilhaException("Número máximo de pilhas atingido!")
            
        elif (resposta == "j"):
            print(p.invertePilha())

        elif (resposta == "z"):
            print(p.esvaziarPilha())

        elif (resposta == "c"):
            print(f"Pilhas criadas: {numdisp}")
            num1, num2 = map(int, (input("Digite duas pilhas: ")).split())
            print(p.concatenaPilha(num1, num2))

        elif (resposta == "m"):
            print(f"Pilhas criadas: {numdisp}")
            esc = int(input("Digite o número da pilha: "))
            if (esc in numdisp):
                pilsel = esc
                print(p.escolherPilha(esc))
            else:
                raise PilhaException("Número inválido")

        elif (resposta == "n"):
            num = int(input("Digite o número: "))
            print(p.converteBin(num))

        elif (resposta == "s"):
            print("Programa encerrado...")
            break    

    except PilhaException as pe:
        print(pe)
    except BaseException as be:
        print(f"Erro desconhecido! {be}")

