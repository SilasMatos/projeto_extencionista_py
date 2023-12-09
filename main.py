
from child import Child
from functions import menu, include_identification_data, include_address_data, include_vaccine_data, list_all_data

def main():
    child = Child()

    while True:
        menu()
        choice = input("Escolha a opção (a-e): ").lower()

        if choice == 'a':
            include_identification_data(child)
        elif choice == 'b':
            include_address_data(child)
        elif choice == 'c':
            include_vaccine_data(child)
        elif choice == 'd':
            list_all_data(child)
        elif choice == 'e':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
