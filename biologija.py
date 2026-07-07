import ollama
import os

# Putanja do tvog Desktopa
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Биологија_80")

# 1. Kreiranje strukture foldera
razredi = ["5_razred", "6_razred", "7_razred", "8_razred"]
for r in razredi:
    os.makedirs(os.path.join(desktop_path, r), exist_ok=True)

# 2. Lista lekcija (primer za 5. razred)
teme_5 = ["Биологија као наука", "Ћелија - грађа и функција", "Микроскоп"]

def generisi_lekciju(tema, razred):
    print(f"Generišem: {tema} za {razred}...")
    
    prompt = f"""
    Napravi HTML fajl za lekciju: {tema}. 
    Pismo: Isključivo ЋИРИЛИЦА.
    DIZAJN:
    - Na vrhu ZLATNA LINIJA (visina 5% ekrana, glassmorphism efekat).
    - Pozadina: Kao školska sveska na linije (svetlije plave linije).
    - 3D MODEL: Ubaci Three.js kod za interaktivni model ćelije koji pulsira na sredini ekrana.
    - SADRŽAJ: Naslov, kratak tekst i poseban crveni box 'ЗА ДВОЈКУ И ЖИВОТ СПАСИ' sa 3 najbitnije stavke.
    - KOD: Daj mi samo čist HTML sa CSS i JS unutra.
    """

    response = ollama.chat(model='gemma2:latest', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    file_name = f"{tema.replace(' ', '_')}.html"
    full_path = os.path.join(desktop_path, razred, file_name)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(response['message']['content'])
    print(f"Uspešno snimljeno u: {full_path}")

# Pokreni za prvu temu
generisi_lekciju(teme_5[0], "5_razred")