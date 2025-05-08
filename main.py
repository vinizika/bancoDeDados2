import random
import string
from supabase import create_client, Client

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
print('[LOCAL] limpa')

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
    print(f'[LOCAL]: {nome}, {endereco}, {capacidade} inserido')
