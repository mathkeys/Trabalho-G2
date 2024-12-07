import time

class Fisico:
    def __init__(self, altura, peso, idade, habilidades):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.habilidades = habilidades

class Habilidades:
    def __init__(self, habilidade1, habilidade2):
        self.habilidade1 = habilidade1
        self.habilidade2 = habilidade2

class Heroi:
    def __init__(self, nome, genero, fisico):
        self.nome = nome
        self.genero = genero
        self.fisico = fisico

    def calcular_dano(self):
        pass

class Guerreiro(Heroi):
    def __init__(self, nome, genero, fisico, forca, armadura):
        super().__init__(nome, genero, fisico)
        self.forca = forca
        self.armadura = armadura
    def calcular_dano(self):
        if self.armadura <= 5:
            return self.forca * 2
        else:
            return (self.forca / 2) + self.armadura

class Arqueiro(Heroi):
    def __init__(self, nome, genero, fisico, destreza, distancia_max, distancia_alvo):
        super().__init__(nome, genero, fisico)
        self.destreza = destreza
        self.distancia_max = distancia_max
        self.distancia_alvo = distancia_alvo

    def calcular_dano(self):
        if self.distancia_alvo > self.distancia_max:
            return self.destreza / 3
        else:
            return self.destreza * 2

herois = []

def obter_valor_validado(nome_atributo):
    while True:
        try:
            valor = int(input(f"Digite o valor para {nome_atributo} (1 a 10): "))
            if 1 <= valor <= 10:
                return valor
            else:
                print("Valor inválido. O valor deve estar entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_idade_validada():
    while True:
        try:
            idade = int(input("Digite a idade do herói: "))
            if idade > 0:
                return idade
            else:
                print("Idade inválida. A idade deve ser maior que 0.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_peso_validado():
    while True:
        try:
            peso = float(input("Digite o peso do herói: "))
            if peso > 0:
                return peso
            else:
                print("Peso inválido. O peso deve ser maior que 0.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def obter_altura_validada():
    while True:
        try:
            altura = float(input("Digite a altura do herói (em metros): "))
            if 0.01 <= altura <= 300:
                return altura
            else:
                print("Altura inválida. A altura deve estar entre 0.01 e 300 metros.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def criar_heroi():
    nome = input("Digite o nome do herói: ")

    while True:
        genero = input("Digite o gênero do herói (masculino/feminino): ").strip().lower()

        if genero in ['masculino', 'masc', 'm']:
            genero_formatado = 'masculino'
            break
        elif genero in ['feminino', 'fem', 'f']:
            genero_formatado = 'feminino'
            break
        else:
            print("Gênero inválido! Por favor, digite 'masculino', 'masc', 'm' ou 'feminino', 'fem', 'f'.")

    print(f"Herói: {nome}, Gênero: {genero_formatado}")

    while True:
        classe = input("Escolha a classe do herói (guerreiro/arqueiro): ").strip().lower()

        if classe in ['guerreiro', 'guerr', 'warrior']:
            classe_formatada = 'guerreiro'
            break
        elif classe in ['arqueiro', 'arq', 'archer']:
            classe_formatada = 'arqueiro'
            break
        else:
            print("Classe inválida! Por favor, digite 'guerreiro', 'guerr', 'warrior' ou 'arqueiro', 'arq', 'archer'.")

    print(f"Herói: {nome}, Gênero: {genero_formatado}, Classe: {classe_formatada}")

    altura = obter_altura_validada()
    peso = obter_peso_validado()
    idade = obter_idade_validada()

    habilidades_disponiveis = [
        "Visão noturna",
        "Fúria",
        "Coragem",
        "Furtividade"
    ]

    print("Escolha duas habilidades para o herói:")
    for i, habilidade in enumerate(habilidades_disponiveis, start=1):
        print(f"{i}. {habilidade}")

    habilidades_selecionadas = []
    while len(habilidades_selecionadas) < 2:
        try:
            escolha = int(input(f"Escolha a habilidade {len(habilidades_selecionadas) + 1} (1 a {len(habilidades_disponiveis)}): "))
            if 1 <= escolha <= len(habilidades_disponiveis):
                habilidade_escolhida = habilidades_disponiveis[escolha - 1]
                if habilidade_escolhida not in habilidades_selecionadas:
                    habilidades_selecionadas.append(habilidade_escolhida)
                else:
                    print("Habilidade já selecionada. Escolha outra.")
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    habilidades = Habilidades(habilidades_selecionadas[0], habilidades_selecionadas[1])
    fisico = Fisico(altura, peso, idade, habilidades)

    if classe_formatada == "guerreiro":
        print("Você criou um guerreiro!")
        forca = obter_valor_validado("força")
        armadura = obter_valor_validado("armadura")
        return Guerreiro(nome, genero_formatado, fisico, forca, armadura)
    elif classe_formatada == "arqueiro":
        print("Você escolheu um arqueiro!")
        destreza = obter_valor_validado("destreza")
        distancia_max = obter_valor_validado("distância máxima")
        distancia_alvo = obter_valor_validado("distância do alvo")
        return Arqueiro(nome, genero_formatado, fisico, destreza, distancia_max, distancia_alvo)
    else:
        print("Classe inválida. O herói não foi criado.")
        return None

def listar_herois(herois):
    if not herois:
        print("Nenhum herói criado.")
    else:
        for i, heroi in enumerate(herois, start=1):
            print(f"{i}. {heroi.nome} - Classe: {type(heroi).__name__}, Altura: {heroi.fisico.altura}m, Peso: {heroi.fisico.peso}kg, Idade: {heroi.fisico.idade}, Habilidades: {heroi.fisico.habilidades.habilidade1}, {heroi.fisico.habilidades.habilidade2}, Dano: {heroi.calcular_dano()}")

def mostrar_menu():
    print("******************************************")
    print("*        BEM-VINDO À CRIAÇÃO DO SEU HERÓI     *")
    print("******************************************")
    time.sleep(1)
    print("Prepare-se para criar e gerenciar seus heróis!")
    time.sleep(1)
    print("\nMenu Principal:")
    print("1. 🌟 Criar novo herói")
    print("2. 📜 Listar heróis")
    print("3. 🚪 Sair")
    print("******************************************")

while True:
    mostrar_menu()
    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        heroi = criar_heroi()
        if heroi:
            herois.append(heroi)
    elif escolha == "2":
        listar_herois(herois)
    elif escolha == "3":
        print("Tchau tchau... Até a próxima aventura!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
