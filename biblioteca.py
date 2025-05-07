class ClassePessoa():
    def __init__(self,nome,idade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.dormindo = False
        self.falando = False
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}"
        f"eu tenho {self.idade} anos e peso {self.peso}")
    def comer (self):
        print(f"A pessoa está comendo")
        if self.dormindo:
            print(f"{self.nome}, não pode comer enquanto está dormindo!")
        elif self.comendo:
            print(f"{self.nome}, já está comendo!")
        elif self.falando:
            print(f"{self.nome}, não pode falar enquanto come")
        else:
            self.comendo = True
            print(f"{self.nome}, não pode comer, porque já está comendo")
    def dormir (self):
        print(f"A pessoa está dormindo")
        if self.comendo:
            print(f"{self.nome}, não pode comer enquanto dorme")
        elif self.falando:
            print(f"{self.nome}, não pode falar enquanto dorme")
        else:
            self.dormindo = True
            print(f"{self.nome}, não pode dormir, pois, já está dormindo")
    def falar (self):
        print(f"A pessoa está falando")
        if self.comendo:
            print(f"{self.nome}, não pode falar enquanto come")
        elif self.dormindo:
            print(f"{self.nome}, não pode dormir enquanto fala")
        else:
            self.falando = True
            print(f"{self.nome}, não pode falar, porque já está falando")