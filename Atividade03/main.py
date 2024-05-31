class ListaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        for contato_nome, contato_telefone in self.contatos.items():
            if contato_nome == nome and contato_telefone == telefone:
                return print(f"O contato {nome} com o telefone {telefone} já existe na lista.")
        self.contatos[nome] = telefone
        return print(f"Contato {nome} com o telefone {telefone} adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            return print(f"Contato {nome} removido com sucesso.")
        return print(f"Contato {nome} não encontrado.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            return print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        return print(f"Contato {nome} não encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            return print("A lista de contatos está vazia.")
        print("Lista de Contatos:")
        for nome, telefone in self.contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
            
def exibir_menu():
    print("Menu:")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Pesquisar Contato")
    print("4. Listar Contatos")
    print("5. Sair")
    
lista = ListaTelefonica()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        lista.adicionar_contato(nome, telefone)
    elif opcao == "2":
        nome = input("Digite o nome do contato a ser removido: ")
        lista.remover_contato(nome)
    elif opcao == "3":
        nome = input("Digite o nome do contato a ser pesquisado: ")
        lista.pesquisar_contato(nome)
    elif opcao == "4":
        lista.listar_contatos()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
