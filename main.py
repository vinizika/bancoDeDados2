import random
import string
from datetime import datetime, timedelta
from supabase import create_client, Client
from collections import Counter
from datetime import datetime, timedelta
import random

url: str = "https://zohjlovkaevbispuxsml.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpvaGpsb3ZrYWV2YmlzcHV4c21sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYzOTU3NDksImV4cCI6MjA2MTk3MTc0OX0.4TMeR8lP4iYUnGko1zaXlCZyVnf6JLuazJy6EiXMGUg"
supabase: Client = create_client(url, key)

#limpar tabela evento
while True:
    ea = supabase.table("evento_artista").select("id_evento,id_artista").execute().data
    if not ea:
        break
    for row in ea:
        supabase.table("evento_artista")\
            .delete().eq("id_evento", row["id_evento"])\
            .eq("id_artista", row["id_artista"]).execute()
print("tabela evento_artista limpa")

#limpar tabela compra_ingresso
while True:
    ci = supabase.table("compra_ingresso").select("id_compra").execute().data
    if not ci:
        break
    for row in ci:
        supabase.table("compra_ingresso")\
            .delete().eq("id_compra", row["id_compra"]).execute()
print("tabela compra_ingresso limpa")

while True:
    compras = supabase.table("compra").select("id_compra").execute().data
    if not compras:
        break
    for row in compras:
        supabase.table("compra").delete().eq("id_compra", row["id_compra"]).execute()
print("tabela delete-compra limpa")

#limpar tabela ingresso
while True:
    ingr = supabase.table("ingresso").select("id_ingresso").execute().data
    if not ingr:
        break
    for r in ingr:
        supabase.table("ingresso").delete().eq("id_ingresso", r["id_ingresso"]).execute()

print("tabela ingresso limpa")

#limpar tabela categoria
while True:
    cats = supabase.table("categoria").select("id_categoria").execute().data
    if not cats:
        break
    for c in cats:
        supabase.table("categoria").delete().eq("id_categoria", c["id_categoria"]).execute()

print("tabela categoria limpa")

#limpar tabela evento
while True:
    eventos = supabase.table("evento").select("id_evento").execute().data
    if not eventos:
        break
    for e in eventos:
        supabase.table("evento").delete().eq("id_evento", e["id_evento"]).execute()

print("tabela evento limpa")

#limpar tabela local
while True:
    registros = supabase.table("local").select("id_local").execute().data
    if not registros:
        break
    for r in registros:
        supabase.table("local").delete().eq("id_local", r["id_local"]).execute()
print('tabela local limpa')

#limpar tabela artista
while True:
    artistas = supabase.table("artista").select("id_artista").execute().data
    if not artistas:
        break
    for a in artistas:
        supabase.table("artista").delete().eq("id_artista", a["id_artista"]).execute()

print("tabela artista limpa")

#limpar tabela pessoa
while True:
    registros = supabase.table("pessoa").select("id_pessoa").execute().data
    if not registros:
        break
    for r in registros:
        supabase.table("pessoa").delete().eq("id_pessoa", r["id_pessoa"]).execute()
    print('tabela pessoa limpa')

#dados fictícios
nomes_locais = [
    "Arena Sol Nascente", "Estádio Vale Verde", "Casa Show Horizonte",
    "Pavilhão Estrela do Norte", "Auditório Lago Azul", "Arena Costa Dourada",
    "Espaço Show Iguatemi", "Estádio Serra Alta", "Casa de Espetáculos Rio Novo",
    "Arena Pedra Branca", "Palco Mar do Sul", "Anfiteatro Pôr-do-Sol",
    "Arena Planalto", "Estação Shows Amazônia", "Mirante Música Viva",
    "Arena Porto do Som", "Terraço Bossa Nova", "Arena Vila Tropical",
    "Espaço Cultural Sertão", "Arena Pampas", "Centro Shows Atlântico",
    "Estádio Monte Azul", "Arena Farol das Estrelas", "Arena Costa Verde",
    "Arena Rio Grande", "Galpão Som & Luz", "Arena Serra Verde",
    "Arena Vale do Som", "Arena Sertão Norte", "Palco Horizonte Livre"
]

primeiros_ruas = [
    "Avenida", "Rua", "Travessa", "Alameda", "Estrada", "Praça",
    "Passeio", "Largo", "Via", "Rotatória", "Caminho", "Boulevard",
    "Estradinha", "Calçadão", "Marginal", "Viela", "Galeria", "Beco",
    "Esplanada", "Jardim", "Vila", "Parque", "Ponte", "Canal",
    "Ramal", "Contorno", "Córrego", "Setor", "Distrito", "Complexo"
]

segundos_ruas = [
    "Faria", "Lima", "Borges", "Moura", "Gonçalves", "Peixoto",
    "Castro", "Almeida", "Ribeiro", "Cardoso", "Machado", "Marques",
    "Pereira", "Nogueira", "Dias", "Teixeira", "Sampaio", "Ferraz",
    "Magalhães", "Campos", "Vargas", "Andrade", "Batista", "Barros",
    "Moreira", "Correia", "Rezende", "Souto", "Vieira", "Guedes"
]

#inserindo registros
for i in range(30):
    nome = nomes_locais[i]
    endereco = f"{primeiros_ruas[i]} {segundos_ruas[i]}, {random.randint(10, 1500)}"
    capacidade = random.randint(15000, 200000)

    supabase.table("local").insert({
        "nome": nome,
        "endereco": endereco,
        "capacidade": capacidade
    }).execute()
    print(f'inserindo na tabela: {nome}, {endereco}, {capacidade} inserido')


#lista de nomes

nomes = [
    "Maria", "Joao", "Ana", "Pedro", "Beatriz", "Carlos", "Mariana", "Felipe",
    "Julia", "Lucas", "Gabriela", "Rafael", "Camila", "Bruno", "Fernanda",
    "Daniel", "Larissa", "Eduardo", "Isabelle", "Gustavo", "Bianca", "Andre",
    "Vitoria", "Rodrigo", "Tatiana", "Alexandre", "Luana", "Henrique",
    "Leticia", "Diego"
]

sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Costa", "Pereira", "Rodrigues",
    "Almeida", "Barbosa", "Lima", "Gomes", "Ribeiro", "Carvalho", "Fernandes",
    "Araujo", "Melo", "Castro", "Rocha", "Martins", "Freitas", "Cardoso",
    "Teixeira", "Pinto", "Monteiro", "Mendes", "Nascimento", "Dias", "Correia",
    "Moreira", "Barros"
]

servidores_email = ["gmail", "outlook", "hotmail", "icloud"]

#aleatoriamente gera datas

inicio = datetime(1960, 1, 1)
fim = datetime(2007, 12, 31)
def data_aleatoria():
    dias = random.randint(0, (fim - inicio).days)
    return (inicio + timedelta(days=dias)).date().isoformat()

#inserindo 30 pessoas aleatórias
for _ in range(30):
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    email = f"{nome.lower()}.{sobrenome.lower()}@{random.choice(servidores_email)}.com"
    cpf = "".join(random.choices("0123456789", k=11))
    dob = data_aleatoria()

    supabase.table("pessoa").insert({
        "nome": f"{nome} {sobrenome}",
        "email": email,
        "cpf": cpf,
        "data_nascimento": dob
    }).execute()
    print(f'inserindo pessoa: {nome}, {sobrenome}, {email}, {cpf}, {dob} inserido')

#lista de artistas e generos
artistas_generos = [
    ("Anitta", "Pop Funk"),
    ("Gusttavo Lima", "Sertanejo"),
    ("Alok", "EDM"),
    ("Ivete Sangalo", "Axé"),
    ("Ludmilla", "Funk Pop"),
    ("Jorge & Mateus", "Sertanejo"),
    ("Marília Mendonça", "Sertanejo"),
    ("Wesley Safadão", "Forró"),
    ("Zé Neto & Cristiano", "Sertanejo"),
    ("Luan Santana", "Sertanejo Pop"),
    ("Pabllo Vittar", "Pop"),
    ("Tiago Iorc", "Folk Pop"),
    ("Djavan", "MPB"),
    ("Gilberto Gil", "MPB"),
    ("Caetano Veloso", "MPB"),
    ("Sandy & Junior", "Pop"),
    ("Skank", "Pop Rock"),
    ("Jota Quest", "Pop Rock"),
    ("Legião Urbana", "Rock"),
    ("Capital Inicial", "Rock"),
    ("Coldplay", "Pop Rock"),
    ("Ed Sheeran", "Pop"),
    ("Beyoncé", "R&B Pop"),
    ("Metallica", "Heavy Metal"),
    ("AC/DC", "Hard Rock"),
    ("Imagine Dragons", "Alternative Rock"),
    ("Dua Lipa", "Pop"),
    ("Billie Eilish", "Indie Pop"),
    ("Bad Bunny", "Reggaeton"),
    ("Karol G", "Reggaeton")
]

#inserindo os artistas
for nome, genero in artistas_generos:
    supabase.table("artista").insert({
        "nome": nome,
        "genero_musical": genero
    }).execute()
    print(f"[INSERE - ARTISTA]: {nome}, {genero} inserido")

#lista de setores 
setores = [
    "Pista", "Pista Premium", "VIP", "Camarote", "Front Stage", "Backstage",
    "Arquibancada", "Cadeira Inferior", "Cadeira Superior", "Mesa", "Lounge",
    "Área VIP", "Balcão", "Mezanino", "Gramado", "Setor Norte", "Setor Sul",
    "Setor Leste", "Setor Oeste", "Deck"
]

#inserindo 10 setores
for setor in random.sample(setores, 10):
    supabase.table("categoria").insert({"nome": setor}).execute()
    print(f"inserindo categoria: {setor} inserido")

#listando aleatoriamente nomes e descricoes de eventos
nomes_evento = [
    "Festival de Música", "Show ao Vivo", "Mega Concerto", "Noite de Sucessos",
    "Turnê Mundial", "Live Session", "Festival Cultural", "Grande Espetáculo",
    "Encontro Musical", "Festa de Verão", "Festa da Música", "Evento Premium",
    "Show Especial", "Tour Brasil", "Evento Exclusivo", "Noite VIP",
    "Concerto Beneficente", "Apresentação Única", "Festival Noturno",
    "Evento Experiência", "Live Experience", "Noite Inesquecível",
    "Festa Open Air", "Festival Anual", "Show de Talentos",
    "Concerto Ao Ar Livre", "Tour Internacional", "Grande Show",
    "Festival Hit", "Live Show"
]

descricoes_evento = [
    "Um evento imperdível para todos os amantes de música.",
    "Uma experiência musical inesquecível.",
    "Venha curtir grandes sucessos ao vivo.",
    "A melhor seleção de artistas em um só palco.",
    "Diversão garantida do início ao fim.",
    "Um espetáculo de luzes e som para encantar.",
    "Celebre a música conosco nesta noite especial.",
    "Emoção e energia em cada apresentação.",
    "Prepare-se para cantar, dançar e vibrar.",
    "O encontro perfeito entre público e artista.",
    "Participe de um show que ficará na memória.",
    "A noite será marcada por grandes emoções.",
    "Um festival pensado para todos os estilos.",
    "Aproveite a vibe e a boa música.",
    "Um evento que vai agitar a cidade.",
    "Ingresso único para uma experiência única.",
    "Uma celebração à arte e à cultura.",
    "O palco setado para momentos inesquecíveis.",
    "Show interativo e cheio de surpresas.",
    "A combinação perfeita de ritmo e performance.",
    "Música de qualidade em um ambiente incrível.",
    "Experiência premium com infraestrutura completa.",
    "Uma noite de grandes hits e novidades.",
    "Para quem gosta de viver o melhor da música.",
    "A energia deste evento vai te contagiar.",
    "Imperdível para fãs e curiosos.",
    "O espetáculo que você estava esperando.",
    "Um show completo para todos os públicos.",
    "Diversos estilos musicais em harmonia.",
    "Um evento épico do começo ao fim."
]

locais_ids   = [l["id_local"]   for l in supabase.table("local").select("id_local").execute().data]
pessoas_ids  = [p["id_pessoa"]  for p in supabase.table("pessoa").select("id_pessoa").execute().data]
#dando aleatoriedade nas datas
inicio = datetime(2020, 1, 1)
fim    = datetime(2028, 12, 31)

def data_aleatoria():
    dias = random.randint(0, (fim - inicio).days)
    return (inicio + timedelta(days=dias)).date().isoformat()

def hora_aleatoria():
    h = random.randint(15, 23)
    m = random.choice([0, 15, 30, 45])
    return f"{h:02d}:{m:02d}:00"

#inserindo 30 eventos na lista
for nome in random.sample(nomes_evento, 30):
    descricao     = random.choice(descricoes_evento)
    data_evento   = data_aleatoria()
    hora_evento   = hora_aleatoria()
    id_local      = random.choice(locais_ids)
    id_organizador = random.choice(pessoas_ids)

    supabase.table("evento").insert({
        "nome": nome,
        "descricao": descricao,
        "data": data_evento,
        "hora": hora_evento,
        "id_local": id_local,
        "id_organizador": id_organizador
    }).execute()

    print(f"inserind evento: {nome}, {data_evento} {hora_evento} inserido")

#listando tipo de ingresso
tipos_ingresso = ["Inteira", "Meia", "PCD", "Meet and Greet", "Popular"]

#listando id do evento e sua categoria
eventos  = supabase.table("evento").select("id_evento", "nome").execute().data
cat_ids  = [c["id_categoria"] for c in supabase.table("categoria").select("id_categoria").execute().data]

#gerando precos pros eventos levando em conta seu tipo
preco_base_evento = {}
for ev in eventos:
    preco_base_evento[ev["id_evento"]] = random.randint(30, 300)
def calcular_preco(base, tipo):
    if tipo.lower() in {"meia", "pcd"}:
        return round(base / 2, 2)
    elif tipo.lower() == "meet and greet":
        return round(base * 1.5, 2)
    elif tipo.lower() == "popular":
        return round(base / 3, 2)
    return round(base, 2) 

#gerando 60 ingressos aleatorios
for _ in range(60):
    evento_escolhido = random.choice(eventos)
    id_evento        = evento_escolhido["id_evento"]
    tipo             = random.choice(tipos_ingresso)
    base_preco       = preco_base_evento[id_evento]
    preco_final      = calcular_preco(base_preco, tipo)
    id_categoria     = random.choice(cat_ids)

    supabase.table("ingresso").insert({
        "tipo": tipo,
        "preco": preco_final,
        "id_evento": id_evento,
        "id_categoria": id_categoria
    }).execute()

    print(f"inserindo ingresso: {tipo}, R$ {preco_final:.2f}, evento {id_evento} inserido")

#lista de formas de pagamento
formas_pgto = ["PIX", "Cartao de credito", "Cartao de debito", "Boleto", "Bitcoin"]
#cache de eventos
eventos = supabase.table("evento").select("id_evento", "data").execute().data
datas_evento = {e["id_evento"]: datetime.fromisoformat(e["data"]) for e in eventos}
#ids de pessoas
ids_pessoas = [p["id_pessoa"] for p in supabase.table("pessoa").select("id_pessoa").execute().data]
#garantindo que todo ingresso terá compras
ingressos = supabase.table("ingresso")\
    .select("id_ingresso", "id_evento").execute().data
#gerando compra de ingressos
for ing in ingressos:
    id_ingresso = ing["id_ingresso"]
    id_evento   = ing["id_evento"]
    data_show   = datas_evento[id_evento] 
    data_min    = data_show - timedelta(days=365)
    data_compra = data_min + timedelta(
        days=random.randint(0, (data_show - data_min).days)
    )
    forma       = random.choice(formas_pgto)
    id_pessoa   = random.choice(ids_pessoas)
    compra_resp = supabase.table("compra").insert({
        "data": data_compra.isoformat(),
        "forma_pagamento": forma,
        "id_pessoa": id_pessoa
    }).execute()

    id_compra = compra_resp.data[0]["id_compra"]

    print(f"inserindo compra: {id_compra}, pessoa {id_pessoa}, "
          f"{data_compra.date()} ({forma}) inserido")
    qtd = random.randint(1, 3)
    supabase.table("compra_ingresso").insert({
        "id_compra": id_compra,
        "id_ingresso": id_ingresso,
        "quantidade": qtd
    }).execute()

    print(f"inserindo compra de ingresso: compra {id_compra}, "
          f"ingresso {id_ingresso}, qtd {qtd} inserido")
evento_ids  = [e["id_evento"]  for e in supabase.table("evento")  .select("id_evento").execute().data]
artista_ids = [a["id_artista"] for a in supabase.table("artista") .select("id_artista").execute().data]
#associando evento e compra
for id_evento in evento_ids:
    artistas_escolhidos = random.sample(artista_ids, random.randint(1, 3))
    #associando evento e artista
    dados = [{"id_evento": id_evento, "id_artista": id_artista}
             for id_artista in artistas_escolhidos]
    supabase.table("evento_artista").insert(dados).execute()
    for id_artista in artistas_escolhidos:
        print(f"inserindo evento e artista: evento {id_evento}, artista {id_artista} inserido")
 
#garantindo que tabelas nao sejam vazias 
def fetch_ids(table, id_field):
    return {row[id_field] for row in supabase.table(table).select(id_field).execute().data}

ids_local     = fetch_ids("local",  "id_local")
ids_pessoa    = fetch_ids("pessoa", "id_pessoa")
ids_categoria = fetch_ids("categoria", "id_categoria")
ids_evento    = fetch_ids("evento", "id_evento")
ids_artista   = fetch_ids("artista", "id_artista")
ids_ingresso  = fetch_ids("ingresso", "id_ingresso")
ids_compra    = fetch_ids("compra", "id_compra")

issues = []
for name, s in [("local", ids_local), ("pessoa", ids_pessoa), ("categoria", ids_categoria),
                ("evento", ids_evento), ("artista", ids_artista),
                ("ingresso", ids_ingresso), ("compra", ids_compra)]:
    if not s:
        issues.append(f"Tabela {name} esta vazia")
        #1-3 artistas por evento
ea_rows = supabase.table("evento_artista").select("id_evento", "id_artista").execute().data
evento_por_artista = Counter()
for ea in ea_rows:
    if ea["id_artista"] not in ids_artista:
        issues.append(f"Evento {ea['id_evento']} tem artista invalido {ea['id_artista']}")
    evento_por_artista[ea["id_evento"]] += 1
for ev in supabase.table("evento").select("*").execute().data:
    n = evento_por_artista.get(ev["id_evento"], 0)
    if n < 1 or n > 3:
        issues.append(f"Evento {ev['id_evento']} tem {n} artistas")
    if ev["id_local"] not in ids_local:
        issues.append(f"Evento {ev['id_evento']} tem id_local invalido {ev['id_local']}")
    if ev["id_organizador"] not in ids_pessoa:
        issues.append(f"Evento {ev['id_evento']} tem id_organizador invalido {ev['id_organizador']}")

ci_rows = supabase.table("compra_ingresso")\
         .select("id_compra", "id_ingresso", "quantidade").execute().data
tickets_comprados = Counter()
for ci in ci_rows:
    if ci["id_ingresso"] not in ids_ingresso:
        issues.append(f"Compra {ci['id_compra']} tem ticket invalido {ci['id_ingresso']}")
    if ci["id_compra"] not in ids_compra:
        issues.append(f"compra_ingresso tem id invalido {ci['id_compra']}")
    if ci["quantidade"] < 1 or ci["quantidade"] > 3:
        issues.append(f"Compra {ci['id_compra']} ticket {ci['id_ingresso']} qtd {ci['quantidade']}")
    tickets_comprados[ci["id_ingresso"]] += ci["quantidade"]

for ing in supabase.table("ingresso").select("id_ingresso", "id_evento", "id_categoria").execute().data:
    if ing["id_evento"] not in ids_evento:
        issues.append(f"Ticket {ing['id_ingresso']} tem id_evento invalido {ing['id_evento']}")
    if ing["id_categoria"] not in ids_categoria:
        issues.append(f"Ticket {ing['id_ingresso']} tem id_categoria invalido {ing['id_categoria']}")
    if tickets_comprados.get(ing["id_ingresso"], 0) == 0:
        issues.append(f"Ticket {ing['id_ingresso']} nao esta linkado a nenhuma compra")
#pelo menos 1 ingresso por show
compra_de_items = {ci["id_compra"] for ci in ci_rows}
for comp in supabase.table("compra").select("id_compra", "id_pessoa").execute().data:
    if comp["id_compra"] not in compra_de_items:
        issues.append(f"Compra {comp['id_compra']} nao tem tickets")
    if comp["id_pessoa"] not in ids_pessoa:
        issues.append(f"Compra {comp['id_compra']} tem id_pessoa invalidos {comp['id_pessoa']}")
#cpfs unicos
pessoas = supabase.table("pessoa").select("cpf", "email", "id_pessoa").execute().data
cpf_count   = Counter(p["cpf"]   for p in pessoas)
email_count = Counter(p["email"] for p in pessoas)
for p in pessoas:
    if cpf_count[p["cpf"]] > 1:
        issues.append(f"CPF duplicado {p['cpf']} (pessoa {p['id_pessoa']})")
    if email_count[p["email"]] > 1:
        issues.append(f"Email dupicado {p['email']} (pessoa {p['id_pessoa']})")

print("\n" + "="*50)
if issues:
    print("teste falhou")
    for msg in issues:
        print(" -", msg)
else:
    print("teste concluido")
print("="*50 + "\n")
