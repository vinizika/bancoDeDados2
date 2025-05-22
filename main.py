import random
import string
from datetime import datetime, timedelta
from supabase import create_client, Client
from collections import Counter
from itertools import product

# configuração do Supabase
url: str = "https://xtqcwyzwxnedqphpnmbs.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh0cWN3eXp3eG5lZHFwaHBubWJzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc5Mzk1MjYsImV4cCI6MjA2MzUxNTUyNn0.wsvIRPsygbZbrrmQkP9o7AUPeFeToQQgp2aQAnSssa4"
supabase: Client = create_client(url, key)

# ── LIMPEZA DE TABELAS (child → parent) ──────────────────────────────────────

# limpar tabela evento_artista
while True:
    rows = supabase.table("evento_artista").select("id_evento,id_artista").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("evento_artista") \
            .delete().eq("id_evento", r["id_evento"]) \
                     .eq("id_artista", r["id_artista"]) \
            .execute()
print("tabela evento_artista limpa")

# limpar tabela evento_pessoa
while True:
    rows = supabase.table("evento_pessoa").select("data_organizacao,id_evento,id_organizador").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("evento_pessoa") \
            .delete().eq("id_evento", r["id_evento"]) \
                     .eq("id_organizador", r["id_organizador"]) \
                     .eq("data_organizacao", r["data_organizacao"]) \
            .execute()
print("tabela evento_pessoa limpa")

# limpar tabela ingresso
while True:
    rows = supabase.table("ingresso").select("id_ingresso").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("ingresso").delete().eq("id_ingresso", r["id_ingresso"]).execute()
print("tabela ingresso limpa")

# limpar tabela compra
while True:
    rows = supabase.table("compra").select("id_compra").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("compra").delete().eq("id_compra", r["id_compra"]).execute()
print("tabela compra limpa")

# limpar tabela categoria
while True:
    rows = supabase.table("categoria").select("id_categoria").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("categoria").delete().eq("id_categoria", r["id_categoria"]).execute()
print("tabela categoria limpa")

# limpar tabela evento
while True:
    rows = supabase.table("evento").select("id_evento").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("evento").delete().eq("id_evento", r["id_evento"]).execute()
print("tabela evento limpa")

# limpar tabela local
while True:
    rows = supabase.table("local").select("id_local").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("local").delete().eq("id_local", r["id_local"]).execute()
print("tabela local limpa")

# limpar tabela artista
while True:
    rows = supabase.table("artista").select("id_artista").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("artista").delete().eq("id_artista", r["id_artista"]).execute()
print("tabela artista limpa")

# limpar tabela pessoa
while True:
    rows = supabase.table("pessoa").select("id_pessoa").execute().data
    if not rows:
        break
    for r in rows:
        supabase.table("pessoa").delete().eq("id_pessoa", r["id_pessoa"]).execute()
print("tabela pessoa limpa")


# ── INSERÇÃO DE DADOS FICTÍCIOS ────────────────────────────────────────────────

# 1) LOCAIS
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
    "Moreira", "Correia", "Rezende", "Souto", "Vieira", "Guedes", "Neves",
    "Tavares",
    "Pimentel",
    "Franco",
    "Azevedo",
    "Monteiro",
    "Aguiar",
    "Soares",
    "Cavalcante",
    "Menezes"
]

combinacoes_ruas = list(product(primeiros_ruas, segundos_ruas))
random.shuffle(combinacoes_ruas)

quantidade = min(random.randint(20, 40), len(combinacoes_ruas), len(nomes_locais))

for i in range(quantidade):
    nome = nomes_locais[i]
    rua1, rua2 = combinacoes_ruas[i]
    endereco = f"{rua1} {rua2}, {random.randint(10, 1500)}"
    capacidade = random.randint(15000, 200000)
    supabase.table("local").insert({
        "nome": nome,
        "endereco": endereco,
        "capacidade": capacidade
    }).execute()
    print(f"[INSERE - LOCAL] {nome} | {endereco} | cap {capacidade}")

# 2) PESSOAS
nomes = [
    "Maria", "Joao", "Ana", "Pedro", "Beatriz", "Carlos", "Mariana", "Felipe",
    "Julia", "Lucas", "Gabriela", "Rafael", "Camila", "Bruno", "Fernanda",
    "Daniel", "Larissa", "Eduardo", "Isabelle", "Gustavo", "Bianca", "Andre",
    "Vitoria", "Rodrigo", "Tatiana", "Alexandre", "Luana", "Henrique",
    "Leticia", "Diego", "Natália",
    "Thiago",
    "Paula",
    "Renato",
    "Aline",
    "Vinícius",
    "Débora",
    "Igor",
    "Simone",
    "Leandro"
]

sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Costa", "Pereira", "Rodrigues",
    "Almeida", "Barbosa", "Lima", "Gomes", "Ribeiro", "Carvalho", "Fernandes",
    "Araujo", "Melo", "Castro", "Rocha", "Martins", "Freitas", "Cardoso",
    "Teixeira", "Pinto", "Monteiro", "Mendes", "Nascimento", "Dias", "Correia",
    "Moreira", "Barros", "Andrade",
    "Farias",
    "Vieira",
    "Ramos",
    "Cavalcante",
    "Peixoto",
    "Tavares",
    "Neves",
    "Miranda",
    "Aguiar"
]
servidores_email = ["gmail", "outlook", "hotmail", "icloud"]

inicio_nasc = datetime(1960, 1, 1)
fim_nasc    = datetime(2007, 12, 31)
def data_nascimento_aleatoria():
    dias = random.randint(0, (fim_nasc - inicio_nasc).days)
    return (inicio_nasc + timedelta(days=dias)).date().isoformat()

# conjunto para registrar pares já usados
pares_utilizados = set()

for _ in range(random.randint(20, 40)):
    while True:
        nome = random.choice(nomes)
        sobrenome = random.choice(sobrenomes)
        par = (nome, sobrenome)
        if par not in pares_utilizados:
            pares_utilizados.add(par)
            break

    email = f"{nome.lower()}.{sobrenome.lower()}@{random.choice(servidores_email)}.com"
    cpf = "".join(random.choices("0123456789", k=11))
    dob = data_nascimento_aleatoria()

    supabase.table("pessoa").insert({
        "nome": f"{nome} {sobrenome}",
        "email": email,
        "cpf": cpf,
        "data_nascimento": dob
    }).execute()

    print(f"[INSERE - PESSOA] {nome} {sobrenome} | {email} | CPF {cpf} | {dob}")

locais_ids   = [l["id_local"]    for l in supabase.table("local").select("id_local").execute().data]
pessoas_ids  = [p["id_pessoa"]   for p in supabase.table("pessoa").select("id_pessoa").execute().data]

# 3) ARTISTAS
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
for nome, gen in artistas_generos:
    supabase.table("artista").insert({
        "nome": nome,
        "genero_musical": gen
    }).execute()
    print(f"[INSERE - ARTISTA] {nome} | {gen}")

# 4) CATEGORIAS (SETOR)
setores = [
    "Pista", "Pista Premium", "VIP", "Camarote", "Front Stage", "Backstage",
    "Arquibancada", "Cadeira Inferior", "Cadeira Superior", "Mesa", "Lounge",
    "Área VIP", "Balcão", "Mezanino", "Gramado", "Setor Norte", "Setor Sul",
    "Setor Leste", "Setor Oeste", "Deck"
]
for setor in random.sample(setores, 10):
    supabase.table("categoria").insert({"nome": setor}).execute()
    print(f"[INSERE - CATEGORIA] {setor}")

cat_ids = [c["id_categoria"] for c in supabase.table("categoria").select("id_categoria").execute().data]

# 5) EVENTOS
nomes_evento = [
    "Festival de Música", "Show ao Vivo", "Mega Concerto", "Noite de Sucessos",
    "Turnê Mundial", "Live Session", "Festival Cultural", "Grande Espetáculo",
    "Encontro Musical", "Festa de Verão", "Festa da Música", "Evento Premium",
    "Show Especial", "Tour Brasil", "Evento Exclusivo", "Noite VIP",
    "Concerto Beneficente", "Apresentação Única", "Festival Noturno",
    "Evento Experiência", "Live Experience", "Noite Inesquecível",
    "Festa Open Air", "Festival Anual", "Show de Talentos",
    "Concerto Ao Ar Livre", "Tour Internacional", "Grande Show",
    "Festival Hit", "Live Show", "Som da Cidade",
    "Vibe Urbana",
    "Show das Estrelas",
    "Ritmos do Brasil",
    "Noite Acústica",
    "Festa das Tribos",
    "Palco Livre",
    "Festival de Estações",
    "Turnê das Lendas",
    "Música Sem Fronteiras"
]

descricoes = [
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
    "Um evento épico do começo ao fim.",
    "Uma jornada sonora que vai mexer com seus sentidos.",
    "O melhor da cena musical reunido em um só lugar.",
    "Ritmos envolventes para uma noite vibrante.",
    "Sinta a batida e deixe-se levar pelo som.",
    "Uma noite repleta de talentos e emoções.",
    "Show com produção de alto nível e grandes artistas.",
    "Uma explosão de cultura, arte e entretenimento.",
    "Curta cada acorde como se fosse o último.",
    "Viva momentos mágicos ao som dos seus favoritos.",
    "O evento musical mais aguardado do ano chegou!"
]

# datas e horas aleatórias
inicio_ev = datetime(2020, 1, 1)
fim_ev    = datetime(2028, 12, 31)
def data_evento_aleatoria():
    dias = random.randint(0, (fim_ev - inicio_ev).days)
    return (inicio_ev + timedelta(days=dias)).date().isoformat()

def hora_evento_aleatoria():
    h = random.randint(15, 23)
    m = random.choice([0, 15, 30, 45])
    return f"{h:02d}:{m:02d}:00"

# cópias das listas para remoção segura
nomes_disponiveis = nomes_evento.copy()
descricoes_disponiveis = descricoes.copy()

# garante que só gere até o número mínimo disponível entre nomes e descrições
quantidade = min(random.randint(20, 40), len(nomes_disponiveis), len(descricoes_disponiveis))

for _ in range(quantidade):
    nome = random.choice(nomes_disponiveis)
    nomes_disponiveis.remove(nome)

    descricao = random.choice(descricoes_disponiveis)
    descricoes_disponiveis.remove(descricao)

    data_ = data_evento_aleatoria()
    hora_ = hora_evento_aleatoria()
    id_local_ = random.choice(locais_ids)

    supabase.table("evento").insert({
        "nome": nome,
        "descricao": descricao,
        "data": data_,
        "hora": hora_,
        "id_local": id_local_
    }).execute()
    print(f"[INSERE - EVENTO] {nome} | {data_} {hora_} | local {id_local_}")


# 6) ORGANIZAÇÃO → evento_pessoa
evento_rows = supabase.table("evento").select("id_evento,data").execute().data
for ev in evento_rows:
    id_ev = ev["id_evento"]
    data_ev = datetime.fromisoformat(ev["data"])
    # entre 2 e 1 anos antes
    inicio_org = data_ev - timedelta(days=730)
    fim_org    = data_ev - timedelta(days=365)
    delta_days = (fim_org - inicio_org).days
    data_org = inicio_org + timedelta(days=random.randint(0, delta_days))
    id_org = random.choice(pessoas_ids)
    supabase.table("evento_pessoa").insert({
        "id_evento": id_ev,
        "id_organizador": id_org,
        "data_organizacao": data_org.date().isoformat()
    }).execute()
    print(f"[INSERE - EVENTO_PESSOA] evento {id_ev} | organizador {id_org} | {data_org.date()}")

# 7) PREÇOS E COMPRAS + INGRESSOS VINCULADOS
tipos_ing = ["Inteira", "Meia", "PCD", "Meet and Greet", "Popular"]
formas_pgto = ["PIX", "Cartao de credito", "Cartao de debito", "Boleto", "Bitcoin"]

# cache base
preco_base = {ev["id_evento"]: random.randint(30, 300) for ev in evento_rows}
datas_ev = {ev["id_evento"]: datetime.fromisoformat(ev["data"]) for ev in evento_rows}

def calc_preco(base, tipo):
    t = tipo.lower()
    if t in {"meia", "pcd"}:
        return round(base/2, 2)
    if t == "meet and greet":
        return round(base*1.5, 2)
    if t == "popular":
        return round(base/3, 2)
    return round(base, 2)

NUM = random.randint(80, 120)
for _ in range(NUM):
    # compra
    id_ev = random.choice(evento_rows)["id_evento"]
    dt_show = datas_ev[id_ev]
    dt_min = dt_show - timedelta(days=365)
    dt_compra = dt_min + timedelta(days=random.randint(0, (dt_show - dt_min).days))
    forma = random.choice(formas_pgto)
    id_pess = random.choice(pessoas_ids)
    resp = supabase.table("compra").insert({
        "data": dt_compra.isoformat(),
        "forma_pagamento": forma,
        "id_pessoa": id_pess
    }).execute()
    id_comp = resp.data[0]["id_compra"]

    # ingresso
    tipo_ = random.choice(tipos_ing)
    preco_ = calc_preco(preco_base[id_ev], tipo_)
    cat_ = random.choice(cat_ids)
    supabase.table("ingresso").insert({
        "tipo": tipo_,
        "preco": preco_,
        "id_evento": id_ev,
        "id_categoria": cat_,
        "id_compra": id_comp
    }).execute()
    print(f"[INSERE - COMPRA+INGRESSO] compra {id_comp} | pessoa {id_pess} | {dt_compra.date()} → ingresso {tipo_} evento {id_ev}")

# 8) ASSOCIAÇÃO EVENTO ↔ ARTISTA
evento_ids  = [e["id_evento"]  for e in evento_rows]
artista_ids = [a["id_artista"] for a in supabase.table("artista").select("id_artista").execute().data]
for ev_id in evento_ids:
    escolhidos = random.sample(artista_ids, random.randint(1, 3))
    dados = [{"id_evento": ev_id, "id_artista": aid} for aid in escolhidos]
    supabase.table("evento_artista").insert(dados).execute()
    for aid in escolhidos:
        print(f"[INSERE - EVENTO_ARTISTA] evento {ev_id} | artista {aid}")

# ── VALIDAÇÕES FINAIS ─────────────────────────────────────────────────────────

# coletar ids existentes
ids_local     = {l["id_local"]   for l in supabase.table("local").select("id_local").execute().data}
ids_pessoa    = {p["id_pessoa"]  for p in supabase.table("pessoa").select("id_pessoa").execute().data}
ids_categoria = {c["id_categoria"] for c in supabase.table("categoria").select("id_categoria").execute().data}
ids_evento    = {e["id_evento"]  for e in supabase.table("evento").select("id_evento").execute().data}
ids_artista   = {a["id_artista"] for a in supabase.table("artista").select("id_artista").execute().data}
ids_ingresso  = {i["id_ingresso"] for i in supabase.table("ingresso").select("id_ingresso").execute().data}
ids_compra    = {c["id_compra"] for c in supabase.table("compra").select("id_compra").execute().data}

issues = []

# validar evento_artista
ea_rows = supabase.table("evento_artista").select("id_evento,id_artista").execute().data
cnt_ev = Counter()
for r in ea_rows:
    if r["id_evento"] not in ids_evento:
        issues.append(f"Evento_artista: evento invalido {r['id_evento']}")
    if r["id_artista"] not in ids_artista:
        issues.append(f"Evento_artista: artista invalido {r['id_artista']}")
    cnt_ev[r["id_evento"]] += 1
for ev_id, n in cnt_ev.items():
    if n < 1 or n > 3:
        issues.append(f"Evento {ev_id} tem {n} artistas (deveria 1–3)")

# validar evento_pessoa
ep_rows = supabase.table("evento_pessoa").select("id_evento,id_organizador,data_organizacao").execute().data
for r in ep_rows:
    if r["id_evento"] not in ids_evento:
        issues.append(f"Evento_pessoa: evento invalido {r['id_evento']}")
    if r["id_organizador"] not in ids_pessoa:
        issues.append(f"Evento_pessoa: organizador invalido {r['id_organizador']}")

# validar ingressos
ing_rows = supabase.table("ingresso") \
    .select("id_ingresso,id_evento,id_categoria,id_compra").execute().data
compras_com_ingresso = set()
for r in ing_rows:
    if r["id_evento"] not in ids_evento:
        issues.append(f"Ingresso {r['id_ingresso']} evento invalido {r['id_evento']}")
    if r["id_categoria"] not in ids_categoria:
        issues.append(f"Ingresso {r['id_ingresso']} categoria invalida {r['id_categoria']}")
    if r["id_compra"] not in ids_compra:
        issues.append(f"Ingresso {r['id_ingresso']} compra invalida {r['id_compra']}")
    compras_com_ingresso.add(r["id_compra"])

# toda compra tem pelo menos 1 ingresso
for comp in supabase.table("compra").select("id_compra,id_pessoa").execute().data:
    cid = comp["id_compra"]
    if cid not in compras_com_ingresso:
        issues.append(f"Compra {cid} não tem ingressos vinculados")
    if comp["id_pessoa"] not in ids_pessoa:
        issues.append(f"Compra {cid} pessoa invalida {comp['id_pessoa']}")

# validar tabela pessoa (CPFs e e-mails únicos)
p_rows = supabase.table("pessoa").select("cpf,email,id_pessoa").execute().data
cpfs   = Counter(p["cpf"]   for p in p_rows)
emails = Counter(p["email"] for p in p_rows)
for p in p_rows:
    if cpfs[p["cpf"]] > 1:
        issues.append(f"CPF duplicado {p['cpf']} (pessoa {p['id_pessoa']})")
    if emails[p["email"]] > 1:
        issues.append(f"Email duplicado {p['email']} (pessoa {p['id_pessoa']})")

# resultado final
print("\n" + "="*60)
if issues:
    print("TESTES FALHARAM:")
    for msg in issues:
        print(" -", msg)
else:
    print("TODOS OS TESTES CONCLUIDOS COM SUCESSO!")
print("="*60 + "\n")
