from menu import show_menu
from extraction import extract_events, extract_red, extract_blue, extract_followers

def main():
    while True:
        show_menu()
        option = input("Elige una opción (1-5): ")
        if option == "1":
            extract_blue()
        elif option == "2":
            extract_events()
        elif option == "3":
            extract_red()
        elif option == "4":
            extract_followers()
        elif option == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
