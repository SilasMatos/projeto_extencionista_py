

from tabulate import tabulate
from child import Child
def menu():
    print("Menu:")
    print("a. Incluir os dados de identificação da criança")
    print("b. Incluir o endereço da criança")
    print("c. Incluir o registro das vacinas da criança")
    print("d. Listar todos os dados da CSC")
    print("e. Sair do Programa")

def include_identification_data(child):
    print("\nIncluir os dados de identificação da criança:")
    child.identification_data['Nome'] = input("Nome da criança: ")
    child.identification_data['Data de nascimento'] = input("Data de nascimento: ")
    child.identification_data['Município de nascimento'] = input("Município de nascimento: ")
    child.identification_data['Nome da mãe'] = input("Nome da mãe: ")
    child.identification_data['Nome do pai'] = input("Nome do pai: ")
    child.identification_data['Telefone do responsável'] = input("Telefone do responsável: ")
    child.identification_data['Etnia'] = input("Etnia (Branca/Negra/Amarela/Parda/Indígena): ")

def include_address_data(child):
    print("\nIncluir o endereço da criança:")
    child.address_data['Logradouro'] = input("Logradouro: ")
    child.address_data['Número'] = input("Número: ")
    child.address_data['Complemento'] = input("Complemento: ")
    child.address_data['Bairro'] = input("Bairro: ")
    child.address_data['Cidade'] = input("Cidade: ")
    child.address_data['CEP'] = input("CEP: ")
    child.address_data['Estado'] = input("Estado: ")

def include_vaccine_data(child):
    print("\nIncluir o registro das vacinas da criança:")

    child.vaccine_data['BCG'] = input("BCG – ID dose única (Sim/Não): ")
    child.vaccine_data['Hepatite B (1)'] = input("Vacina contra hepatite B (1ª dose) (Sim/Não): ")

    age = int(input("Idade da criança (em meses): "))

    if age < 5:
        child.vaccine_data['Hepatite B (2)'] = input("Vacina contra hepatite B (2ª dose) (Sim/Não): ")
        child.vaccine_data['Tetravalente (DTP + Hib) (1)'] = input("Vacina tetravalente (DTP + Hib) 1ª dose (Sim/Não): ")
        child.vaccine_data['VOP (1)'] = input("VOP (vacina oral contra pólio) 1ª dose (Sim/Não): ")
        child.vaccine_data['VORH (1)'] = input("VORH (Vacina Oral de Rotavírus Humano) 1ª dose (Sim/Não): ")

        if age == 2:
            child.vaccine_data['Tetravalente (DTP + Hib) (2)'] = input("Vacina tetravalente (DTP + Hib) 2ª dose (Sim/Não): ")

        elif age == 4:
            child.vaccine_data['VOP (2)'] = input("VOP (vacina oral contra pólio) 2ª dose (Sim/Não): ")
            child.vaccine_data['VORH (2)'] = input("VORH (Vacina Oral de Rotavírus Humano) 2ª dose (Sim/Não): ")

    else:
        print("A idade da criança deve ser inferior a 5 meses para inclusão dessas vacinas.")

def list_all_data(child):
    print("\nDados da CSC:")
    print("Identificação:")
    for key, value in child.identification_data.items():
        print(f"{key}: {value}")

    print("\nEndereço:")
    for key, value in child.address_data.items():
        print(f"{key}: {value}")

    print("\nRegistro das vacinas:")
    vaccine_data_table = []
    for key, value in child.vaccine_data.items():
        vaccine_data_table.append([key, value])

    print(tabulate(vaccine_data_table, headers=["Vacina", "Dose"], tablefmt="grid"))