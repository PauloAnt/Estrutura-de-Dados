import numpy as np

class PilhaException(Exception):
    def __init__(self, mensagem):
        super.__init__(mensagem)

class Pilha():
    pilhas = {}
    pilhas_conc = {}
    def __init__(self, size:int=10):
        self.__pilhaatual = Pilha.pilhas[1] = [np.full(size, None), -1]

    def __str__(self)->str:
        s = '[ ' 
        for i in range(self.__pilhaatual[1] + 1):
            s += f'{self.__pilhaatual[0][i]}, '
        s = s.rstrip(', ')
        s += ' ]'
        return s
    
    def __len__(self):
        return self.__pilhaatual[1] + 1

    def estaVazia(self):
        if (self.__pilhaatual[1] == -1):
            return True
        return False
    
    def estaCheia(self):
        if (self.__pilhaatual[1] == len(self.__pilhaatual) + 1):
            return True
        return False
    
    def topo(self):
        return self.__pilhaatual[0][1]

    def empilha(self, carga):   
        if self.estaCheia():
            raise PilhaException("A pilha está cheia")
        self.__pilhaatual[1] += 1
        self.__pilhaatual[0][self.__pilhaatual[1]] = carga

    def desempilha(self):
        if self.estaVazia():
            raise PilhaException("A pilha está vázia")
        carga = self.__pilhaatual[0][self.__pilhaatual[1]]
        self.__pilhaatual[1] -= 1
        return carga

    def busca(self, elemento):
        if (elemento not in self.__pilhaatual):
            raise PilhaException("O item não está na pilha")
        for i in range(self.__pilhaatual[1]):
            if (self.__pilhaatual[0][i] == elemento):
                return self.__pilhaatual[0][i]
            
    def elemento(self, chave):
        if (chave > 0 and chave <= self.__pilhaatual[1]):
            return self.__pilhaatual[0][chave]
        else:
            raise PilhaException(f"O número deve ser de 1 a {self.__pilhaatual[1]}")

    @classmethod  
    def criarPilha(cls, num, tam):
            cls.pilhas[num] = [np.full(tam, None), -1]
            return f"Pilha criada com sucesso! {cls.pilhas[num][0]}"

    def escolherPilha(self, num):
        if (num in Pilha.pilhas.keys()):
            self.__pilhaatual = Pilha.pilhas[num]
            return f"Pilha selecionada: {self.__pilhaatual[0]}"
        else:
            raise PilhaException(f"Número inválido, escolha de 1 a {len(Pilha.pilhas)}")    
    
    def invertePilha(self):
        if (self.estaVazia()):
            return "A pilha está vázia."
        self.__pilhaatual[0] = self.__pilhaatual[0][self.__pilhaatual[1]::-1]
        return self.__pilhaatual[0]
    
    def esvaziarPilha(self):
        if (self.estaVazia()):
            return "A pilha já está vázia."
        self.__pilhaatual = [np.full(len(self.__pilhaatual[0]), None), -1]
        return self.__pilhaatual[0]
        
    @classmethod
    def concatenaPilha(cls, p1, p2):
        cls.pilhas_conc[(p1,p2)] = []
        for i in range(cls.pilhas[p1][1] + 1):
            cls.pilhas_conc[(p1,p2)].append(cls.pilhas[p1][0][i])
        for i in range(cls.pilhas[p2][1] + 1):
            cls.pilhas_conc[(p1,p2)].append(cls.pilhas[p2][0][i])
        return cls.pilhas_conc[(p1,p2)]

    def converteBin(self, num):
        num_bin = bin(num)
        num_bin = num_bin.lstrip("0b")
        return num_bin