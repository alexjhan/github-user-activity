from tabulate import tabulate
import requests

input_username = input("Enter your username: ")
if input_username == "":
    print("❌ Error: No se ha ingresado un nombre de usuario.")
    exit()
url_profile = f'https://api.github.com/users/{input_username}'
response = requests.get(url_profile)
if response.status_code == 200:
        print(f"✅ Perfil encontrado: {input_username}")
        url_events='https://api.github.com/users/'+input_username+'/events' # URL to get the user's events
        url_red='https://api.github.com/users/'+input_username+'/repos' # URL to get the user's repos
        url_blue='https://api.github.com/users/'+input_username # URL to get the user's profile
        url_followers='https://api.github.com/users/'+input_username+'/followers' # URL to get the user's followers

        def extract_events():
            response = requests.get(url_events).json()
            # Crear una lista de datos específicos
            extracted_data = [
                [event.get("type"), event.get("repo", {}).get("name"), event.get("created_at")]
                for event in response
            ]
            # Encabezados para la tabla
            headers = ["Tipo de evento", "Nombre del repositorio", "Fecha de creación"]
            # Mostrar la tabla formateada
            print(tabulate(extracted_data, headers, tablefmt="grid"))
        def extract_red():
            response = requests.get(url_red).json()
            # Extraer información específica de los repositorios
            extracted_data = [
                        [repo.get("name"), repo.get("html_url"), repo.get("language"), repo.get("created_at")]
                        for repo in response
                    ]
            # Encabezados para la tabla
            headers = ["Nombre del Repositorio", "URL", "Lenguaje", "Fecha de Creación"]
            # Mostrar la tabla formateada
            print(tabulate(extracted_data, headers, tablefmt="grid"))
        def extract_blue():
            response = requests.get(url_blue).json()
            extracted_data = [
                ["Nombre de Usuario", response["login"]],
                ["ID", response["id"]],
                ["Nombre", response.get("name", "No especificado")],
                ["Compañía", response.get("company", "No especificado")],
                ["Blog", response.get("blog", "No especificado")],
                ["Ubicación", response.get("location", "No especificado")],
                ["Bio", response.get("bio", "No especificado")],
                ["Twitter", response.get("twitter_username", "No especificado")],
                ["Repos Públicos", response["public_repos"]],
                ["Seguidores", response["followers"]],
                ["Siguiendo", response["following"]],
                ["Fecha de Creación", response["created_at"]],
            ]
            # Mostrar la tabla
            print(tabulate(extracted_data, headers=["Campo", "Valor"], tablefmt="grid"))
        def extract_followers():    
            response = requests.get(url_followers).json()
            # Extraer información específica de cada seguidor
            followers_data = [
                [follower["login"], follower["id"], follower["html_url"]]
                for follower in response
            ]

            # Mostrar los datos en una tabla
            print(tabulate(followers_data, headers=["Nombre de Usuario", "ID", "Perfil URL"], tablefmt="grid"))
elif response.status_code == 404:
    print(f"❌ Error: El perfil '{input_username}' no existe en GitHub.")
    exit()