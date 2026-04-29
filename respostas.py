import random

saudacoes = [
    "E aí, {nome}! Como você tá hoje?",
    "Oi, {nome}! Bom te ver de novo.",
    "Salve, {nome}! O que manda?"
]

tristeza = [
    "Poxa... sinto que você não tá no seu melhor, {nome}. Mas isso passa.",
    "Tô contigo, {nome}. Às vezes pesa mesmo.",
    "Respira um pouco, {nome}. Você aguenta mais do que imagina."
]

felicidade = [
    "Aí sim, {nome}! Essa energia é boa demais.",
    "Fico feliz por você, {nome}. De verdade.",
    "Que vibe boa, {nome}!"
]

neutras = [
    "Entendi, {nome}. Quer continuar?",
    "Beleza, {nome}. Manda mais.",
    "Tô ouvindo, {nome}."
]

desconhecido = [
    "Não sei se entendi direito, {nome}, mas continua.",
    "Fala mais sobre isso, {nome}.",
    "Às vezes é confuso mesmo, {nome}."
]

raiva = [
         "calma ai, {nome}, vai dar tudo certo.",
         "fique de boa {nome}, no final o bem sempre vence.",
         "eu te entendo {nome}, to bolado tmb, pega essa raiva e usa de combustivel."
]

despedida = [
    "Até mais, {nome}! Cuida bem de você.",
    "Tchau, {nome}! Volta quando quiser.",
    "Foi bom falar contigo, {nome}. Até a próxima!" 
]

nãoidentificado = [ "não entendi {nome}, qual o seu sentimento de agora?"
                   "como assim {nome}? Como você está se sentindo"
]

defelicidadeparatristeza = [
    "{nome}, a vida da dessas, assim como uma montanha russa, o mais importaante é entender seus sentimentos e tentar mudar a situação"
    "{nome}, assim como sua felicidade sumiu ela aparecerá novamente, #tudopassa"

]                   

detristezaparafelicidade = [
    "Ai sim {nome} fico feliz que você está bem agora, assim que se faz"    

] 
 
deraivaparatristeza = [
    "Os seus animos estão acalmando, você vai encontrar a melhor forma de contornar essa situação #confio"

] 

deraivaparafelicidade = [
    "Ai sim {nome}, deixou aquela revolta de lado, o melhor é viver feliz e bem consigo mesmo"
]

defelicidadepararaiva = [
    "{nome}, no mesmo nível de intensidade de felicidade que você estava agora, use essa revolta a seu favor e resolva esse problema (sem perder a cabeça, é claro #vcconsegue)"
]

detristezapararaiva = [
    "{nome}, sei que não está fácil, mas tente relaxar antes que você faça algo que se arrependa futuramente"
]

triste_persistente = [
    "{nome}, se a vida fosse uma constante de prazer e gozo não valeria a pena, os desafios são feitos para nos forjar, assim como disse Nietzsche- Aquilo que não me mata só me deixa mais forte"
]

def escolher(lista, nome):
    return random.choice(lista).format(nome=nome)
