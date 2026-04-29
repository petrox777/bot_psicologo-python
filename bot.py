import time
from respostas import ( # Importando as listas de respostas 
    saudacoes, tristeza, felicidade, neutras, desconhecido, despedida, raiva, nãoidentificado, escolher
)

def iniciar_bot(): 
    nome = None # Variável para armazenar o nome do usuário

    # Inicializando a variável memoria
    memoria = { # Dicionário para armazenar o humor e contadores
        "humor_atual": None,
        "contador_triste": 0,
        "contador_feliz" : 0,
        "contador_raiva" : 0,
        "humor_anterior": None,
        "historico": []
    }




    print("Iniciando boa vibração...")
    time.sleep(1)
    print("Carregando empatia premium...")
    time.sleep(1)
    print("Tudo pronto! Pode falar comigo.\n")

    while True:
        if nome is None:
            nome = input("Qual é o seu nome? ").strip() # Perguntando o nome do usuário
            print(f"Prazer, {nome}! Agora sim.")
            continue

        user = input("> ").lower() # Lendo a entrada do usuário

        if any(p in user for p in ["sair", "exit", "quit"]):
            resposta = escolher(despedida, nome)
            print(resposta)
            break

        if any(p in user for p in ["oi", "ola", "salve", "opa", "hey"]):
            resposta = print(escolher(saudacoes, nome))

        elif any(p in user for p in ["triste", "mal", "chateado", "sozinho"]):
            memoria["humor"] = "triste"
            memoria["contador_triste"] += 1

            print("DEBUG -> contador_triste:", memoria["contador_triste"])

            if memoria["contador_triste"] >= 5:
                print(f"{nome}, fica assim não, vc é d++, bola pra frente")
            elif memoria["contador_triste"] >= 3 and memoria["contador_feliz"] >= 0:
                print("triste_persistente")
            else:
                print(escolher(tristeza, nome))
    

        elif any(p in user for p in ["feliz", "top", "bom", "ótimo"]):
            memoria["humor"] = "feliz"
            memoria["contador_feliz"] += 1

            if memoria["contador_feliz"] >= 2:
             print(f"oi, {nome}, ai sim pô, ninguém te para!!!")
            else:
               resposta = print(escolher(felicidade, nome))

        elif any(p in user for p in ["nada", "de boa", "suave"]):
            resposta = print(escolher(neutras, nome))

        elif any(p in user for p in ["raiva", "furia", "revoltado" , "revoltada"]):
            resposta = print(escolher(raiva, nome))
            memoria["contador_raiva"] += 1        
           
            if memoria["contador_raiva"] >= 3:
                print(f"não explode {nome}, deixa tudo de lado e vai fazer algo que você goste")


        elif user.strip() == "":
            resposta = print(escolher(nãoidentificado, nome))
        
        else:
            resposta = print(escolher(nãoidentificado, nome))

