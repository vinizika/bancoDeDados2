import random
import string
from supabase import create_client, Client # type: ignore

url: str = "https://zohjlovkaevbispuxsml.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpvaGpsb3ZrYWV2YmlzcHV4c21sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYzOTU3NDksImV4cCI6MjA2MTk3MTc0OX0.4TMeR8lP4iYUnGko1zaXlCZyVnf6JLuazJy6EiXMGUg"
supabase: Client = create_client(url, key)


# ─── LIMPA A TABELA LOCAL ──────────────────────────────────────────────────────
while True:
    registros = supabase.table("local").select("id_local").execute().data
    if not registros:
        break
    for r in registros:
        supabase.table("local").delete().eq("id_local", r["id_local"]).execute()
print('[DELETA - LOCAL] limpa')

# ─── LISTAS DE DADOS FICTÍCIOS ─────────────────────────────────────────────────
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

# ─── INSERE OS NOVOS REGISTROS ─────────────────────────────────────────────────
for i in range(30):
    nome = nomes_locais[i]
    endereco = f"{primeiros_ruas[i]} {segundos_ruas[i]}, {random.randint(10, 1500)}"
    capacidade = random.randint(15000, 200000)

    supabase.table("local").insert({
        "nome": nome,
        "endereco": endereco,
        "capacidade": capacidade
    }).execute()
    print(f'[INSERE - LOCAL]: {nome}, {endereco}, {capacidade} inserido')

from datetime import datetime, timedelta
import random

# ─── LIMPA A TABELA PESSOA ─────────────────────────────────────────────────────
while True:
    registros = supabase.table("pessoa").select("id_pessoa").execute().data
    if not registros:
        break
    for r in registros:
        supabase.table("pessoa").delete().eq("id_pessoa", r["id_pessoa"]).execute()
    print('[DELETA - PESSOA] limpa')

# ─── LISTAS DE NOMES E SOBRENOMES ──────────────────────────────────────────────
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

# ─── FUNÇÃO PARA DATA DE NASCIMENTO ALEATÓRIA ────────────────────────────────
inicio = datetime(1960, 1, 1)
fim = datetime(2007, 12, 31)
def data_aleatoria():
    dias = random.randint(0, (fim - inicio).days)
    return (inicio + timedelta(days=dias)).date().isoformat()

# ─── INSERE 30 PESSOAS ─────────────────────────────────────────────────────────
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
    print(f'[INSERE - PESSOA]: {nome}, {sobrenome}, {email}, {cpf}, {dob} inserido')

# ─── LIMPA A TABELA ARTISTA ────────────────────────────────────────────────────
while True:
    artistas = supabase.table("artista").select("id_artista").execute().data
    if not artistas:
        break
    for a in artistas:
        supabase.table("artista").delete().eq("id_artista", a["id_artista"]).execute()

print("[DELETE - ARTISTA]: tabela artista limpa com sucesso.")

# ─── LISTA DE ARTISTAS E SEUS GÊNEROS ─────────────────────────────────────────
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

# ─── INSERE OS ARTISTAS ───────────────────────────────────────────────────────
for nome, genero in artistas_generos:
    supabase.table("artista").insert({
        "nome": nome,
        "genero_musical": genero
    }).execute()
    print(f"[INSERE - ARTISTA]: {nome}, {genero} inserido")

# ─── LIMPA A TABELA CATEGORIA ─────────────────────────────────────────────────
while True:
    cats = supabase.table("categoria").select("id_categoria").execute().data
    if not cats:
        break
    for c in cats:
        supabase.table("categoria").delete().eq("id_categoria", c["id_categoria"]).execute()

print("[DELETE - CATEGORIA]: tabela categoria limpa com sucesso.")

# ─── LISTA DE SETORES / ÁREAS DO LOCAL ────────────────────────────────────────
setores = [
    "Pista", "Pista Premium", "VIP", "Camarote", "Front Stage", "Backstage",
    "Arquibancada", "Cadeira Inferior", "Cadeira Superior", "Mesa", "Lounge",
    "Área VIP", "Balcão", "Mezanino", "Gramado", "Setor Norte", "Setor Sul",
    "Setor Leste", "Setor Oeste", "Deck"
]

# ─── INSERE 10 SETORES (SEM REPETIÇÃO) ───────────────────────────────────────
for setor in random.sample(setores, 10):
    supabase.table("categoria").insert({"nome": setor}).execute()
    print(f"[INSERE - CATEGORIA]: {setor} inserido")

# ─── LIMPA A TABELA EVENTO ────────────────────────────────────────────────────
while True:
    eventos = supabase.table("evento").select("id_evento").execute().data
    if not eventos:
        break
    for e in eventos:
        supabase.table("evento").delete().eq("id_evento", e["id_evento"]).execute()

print("[DELETE - EVENTO]: tabela evento limpa com sucesso.")

# ─── LISTAS GENÉRICAS DE NOMES E DESCRIÇÕES ───────────────────────────────────
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

# ─── COLETA IDs VÁLIDOS DE LOCAL E PESSOA ─────────────────────────────────────
locais_ids   = [l["id_local"]   for l in supabase.table("local").select("id_local").execute().data]
pessoas_ids  = [p["id_pessoa"]  for p in supabase.table("pessoa").select("id_pessoa").execute().data]

# ─── FUNÇÕES DE DATA E HORA ALEATÓRIAS ────────────────────────────────────────
inicio = datetime(2020, 1, 1)
fim    = datetime(2028, 12, 31)

def data_aleatoria():
    dias = random.randint(0, (fim - inicio).days)
    return (inicio + timedelta(days=dias)).date().isoformat()

def hora_aleatoria():
    h = random.randint(15, 23)  # eventos geralmente à noite
    m = random.choice([0, 15, 30, 45])
    return f"{h:02d}:{m:02d}:00"

# ─── INSERE 30 EVENTOS ────────────────────────────────────────────────────────
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

    print(f"[INSERE - EVENTO]: {nome}, {data_evento} {hora_evento} inserido")

