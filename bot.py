import time
from respostas import ( # Importando as listas de respostas 
    saudacoes, tristeza, felicidade, neutras, despedida, raiva, não_identificado, de_tristeza_para_raiva, de_tristeza_para_felicidade, triste_persistente, de_raiva_para_tristeza, de_raiva_para_felicidade, de_felicidade_para_raiva, de_felicidade_para_tristeza, de_tristeza_para_neutralidade, escolher
)
def interpretar_memoria(memoria):

    if {"contador_triste"}>= 5:
        return "triste_pesado"

    elif {"contador_feliz"} > 3:
        return "felicidade"
    
    elif {"contador_triste"} >= 3:
        return "triste_persistente"
    
    elif {"contador_feliz"} >= 3:
        return "muita_felicidade"
    
    elif {"contador_raiva"} >= 3:
        return "raiva_persistente"
    
    elif {"humor_anterior"} == "triste" and {"humor_atual"} == "raiva":
        return "de_tristeza_para_raiva"
    
    elif {"humor_anterior"} == "triste" and {"humor_atual"} == "feliz":
        return "de_tristeza_para_felicidade"
    
    elif {"humor_anterior"} == "raiva" and {"humor_atual"} == "triste":
        return "de_raiva_para_tristeza"
    
    elif {"humor_anterior"} == "raiva" and {"humor_atual"} == "feliz":
        return "de_raiva_para_felicidade"
    
    elif {"humor_anterior"} == "feliz" and {"humor_atual"} == "raiva":
        return "de_felicidade_para_raiva"
    
    elif {"humor_anterior"} == "feliz" and {"humor_atual"} == "triste":
        return "de_felicidade_para_tristeza"            
    
    elif {"humor_anterior"} == "triste" and {"humor_atual"} == "neutro":
        return "de_tristeza_para_neutralidade"
    
    return "não_identificado"


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
            print(escolher(despedida, nome))
            break

        if any(p in user for p in ["oi", "ola", "salve", "opa", "hey"]):
            print(escolher(saudacoes, nome))

        if any(p in user for p in ["triste", "mal", "chateado", "sozinho"]):
            memoria["humor_anterior"] = memoria["humor_atual"] 
            memoria["humor_atual"] = "triste"
            memoria["contador_triste"] += 1

            
            if estado == "de_tristeza_para_raiva":
                print(escolher(de_tristeza_para_raiva, nome))

            elif estado == "de_tristeza_para_felicidade":
                print(escolher(de_tristeza_para_felicidade, nome))

            elif estado == "triste_persistente":
                 print(escolher(triste_persistente, nome))    


            print("DEBUG -> contador_triste:", memoria["contador_triste"])

            if memoria["contador_triste"] >= 5:
                print(f"{nome}, fica assim não, vc é d++, bola pra frente")
            elif memoria["contador_triste"] >= 3 and memoria["contador_feliz"] >= 0:
                print( f"{nome}, se a vida fosse uma constante de prazer e gozo não valeria a pena, os desafios são feitos para nos forjar, assim como disse Nietzsche- Aquilo que não me mata só me deixa mais forte")
            else:
                print(escolher(tristeza, nome))
    

        elif any(p in user for p in ["feliz", "top", "bom", "ótimo"]):
            memoria["humor_anterior"] = memoria["humor_atual"]
            memoria["humor_atual"]= "feliz"
            memoria["contador_feliz"] += 1

            if estado =="de_tristeza_para_felicidade":
               print(escolher(de_tristeza_para_felicidade, nome))

            if estado == "de_raiva_para_felicidade":
               print(escolher(de_raiva_para_felicidade, nome))         

            if memoria["contador_feliz"] >= 3:
               print(f"oi, {nome}, ai sim pô, ninguém te para!!!")

            if estado == "felicidade":
               print(escolher(felicidade, nome))

        elif any(p in user for p in ["nada", "de boa", "suave"]):
            print(escolher(neutras, nome))

        elif any(p in user for p in ["raiva", "furia", "revoltado" , "revoltada"]):
            print(escolher(raiva, nome))
            memoria["contador_raiva"] += 1        
           
            if memoria["contador_raiva"] >= 3:
                print(f"não explode {nome}, deixa tudo de lado e vai fazer algo que você goste")


        elif user.strip() == "":
           print(escolher(não_identificado, nome))
        
        else:
           print(escolher(não_identificado, nome))
