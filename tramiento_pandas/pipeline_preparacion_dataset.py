# -*- coding: utf-8 -*-
"""
Pipeline de preparación de datasets (script equivalente al notebook).
Ejecuta:  python pipeline_preparacion_dataset.py
Genera:   tickets_soporte.xlsx (si no existe) y tickets_soporte_limpio.xlsx / .parquet
"""
import re, os, random
from pathlib import Path
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

RAW_XLSX = Path("tickets_soporte.xlsx")
CLEAN_PATH_XLSX = Path("tickets_soporte_limpio.xlsx")
CLEAN_PATH_PARQUET = Path("tickets_soporte_limpio.parquet")

random.seed(42); np.random.seed(42)

def ensure_raw_dataset():
    if RAW_XLSX.exists():
        return pd.read_excel(RAW_XLSX)
    N = 5000
    nombres = ['Carlos','Ana','Luis','María','Juan','Sofía','Pedro','Lucía','Miguel','Elena','Andrés','Valeria','Diego','Camila','Jorge','Paula','Ricardo','Fernanda','Héctor','Gabriela']
    dominios = ['gmail.com','outlook.com','empresa.com','hotmail.com','yahoo.com']
    productos = ['router','laptop','impresora','telefono','monitor','mouse','teclado','software crm','licencia antivirus','tablet']
    canales = ['email','chat','telefono','web']
    categorias = ['soporte','producto','marketing','otro']
    idiomas = ['es','en','pt']
    issues = ['no enciende','no conecta a wifi','pantalla azul','no imprime','error de licencia','lento al iniciar','se reinicia solo','no carga la bateria','no reconoce usb','temperatura alta']
    infos = ['precio y disponibilidad','caracteristicas tecnicas','compatibilidad con software','opciones de garantia','manual de usuario','accesorios disponibles']
    def random_phone():
        fmts = [lambda: f'+52 55 {random.randint(1000,9999)} {random.randint(1000,9999)}',
                lambda: f'55{random.randint(10000000,99999999)}',
                lambda: f'(55) {random.randint(1000,9999)}-{random.randint(1000,9999)}',
                lambda: f'{random.randint(6000000000,7999999999)}']
        return random.choice(fmts)()
    def random_email(nombre):
        base=(nombre.lower().replace('í','i').replace('á','a').replace('é','e').replace('ó','o').replace('ú','u'))
        return f"{base}{random.randint(1,999)}@{random.choice(dominios)}"
    def random_date(start_days=200):
        start = datetime.now() - timedelta(days=start_days)
        return (start + timedelta(days=random.randint(0,start_days))).date().isoformat()
    def build_text(nombre, email, phone, producto, categoria, idioma):
        if categoria=='soporte':
            if idioma=='es':
                t = random.choice([
                    f"Hola, soy {nombre}. Tengo un problema con el {producto}: {random.choice(issues)}. Mi correo es {email} y mi telefono es {phone}. Pueden ayudarme por favor?",
                    f"Buenas, {nombre} por aqui. El {producto} presenta {random.choice(issues)}. Contacto: {email} {phone}. Gracias!",
                    f"{nombre} reporta fallo en {producto}. Detalle: {random.choice(issues)}. Email {email} tel {phone}."
                ])
            elif idioma=='en':
                t = f"Hi, I'm {nombre}. I have an issue with the {producto}: {random.choice(issues)}. Email {email}, phone {phone}."
            else:
                t = f"Olá, sou {nombre}. Tenho um problema com o {producto}: {random.choice(issues)}. Email {email}, telefone {phone}."
        elif categoria=='producto':
            if idioma=='es':
                t = f"Quiero informacion sobre {producto}: {random.choice(infos)}. Mi correo {email} y tel {phone}."
            elif idioma=='en':
                t = f"I want information about {producto}: {random.choice(infos)}. Contact {email} {phone}."
            else:
                t = f"Quero informacoes sobre {producto}: {random.choice(infos)}. Contato {email} {phone}."
        elif categoria=='marketing':
            t = "Suscribete a nuestro boletin y recibe grandes ofertas!!!   ### %%    "
        else:
            t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. ### fuera de contexto"
        return re.sub(r"\s{2,}", "  ", t)
    rows = []
    for i in range(N):
        nombre = random.choice(nombres)
        email = random_email(nombre)
        phone = random_phone()
        idioma = random.choices(population=idiomas, weights=[0.78,0.15,0.07], k=1)[0]
        categoria = random.choices(population=categorias, weights=[0.6,0.2,0.15,0.05], k=1)[0]
        producto = random.choice(productos)
        canal = random.choice(canales)
        asunto = random.choice(['Consulta','Incidencia','Reclamo','Seguimiento','Soporte urgente','Info producto','Solicitud','Error sistema'])
        texto = build_text(nombre, email, phone, producto, categoria, idioma)
        if random.random()<0.02: producto=np.nan
        if random.random()<0.02: phone=np.nan
        if random.random()<0.01: email=np.nan
        if random.random()<0.01: texto=np.nan
        rows.append({'id':i+1,'fecha':random_date(),'canal':canal,'nombre':nombre,'email':email,'telefono':phone,'idioma':idioma,'categoria':categoria,'producto':producto,'asunto':asunto,'texto':texto,'prioridad':random.choice(['alta','media','baja']),'estado':random.choice(['abierto','en_proceso','resuelto'])})
    df_raw = pd.DataFrame(rows)
    df_raw.to_excel(RAW_XLSX, index=False)
    return df_raw

def normalize_spaces_punct(s: pd.Series)->pd.Series:
    s=s.str.replace(r'\s+',' ',regex=True)
    s=s.str.replace(r'\s+([,.;:!?])',r'\1',regex=True)
    s=s.str.replace(r'([,.;:!?])(\S)',r'\1 \2',regex=True)
    return s.str.strip()

def mask_pii(text):
    email_pat=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.\-]+')
    phone_pat=re.compile(r'(\+?\d[\d\s\-()]{7,}\d)')
    nombres=['Carlos','Ana','Luis','María','Juan','Sofía','Pedro','Lucía','Miguel','Elena','Andrés','Valeria','Diego','Camila','Jorge','Paula','Ricardo','Fernanda','Héctor','Gabriela']
    if not isinstance(text,str): return text
    text=email_pat.sub('[EMAIL]',text)
    text=phone_pat.sub('[TEL]',text)
    for n in nombres:
        text=re.sub(rf'\b{re.escape(n)}\b','[NOMBRE]',text)
        text=re.sub(rf'\b{re.escape(n.lower())}\b','[NOMBRE]',text)
    text=re.sub(r'\b(soy|mi nombre es)\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+',r'\1 [NOMBRE]',text,flags=re.IGNORECASE)
    return text

def lowercase_preserve_tags(s: pd.Series)->pd.Series:
    s_low=s.str.lower()
    s_low=s_low.str.replace(r'\[email\]','[EMAIL]',regex=True)
    s_low=s_low.str.replace(r'\[tel\]','[TEL]',regex=True)
    s_low=s_low.str.replace(r'\[nombre\]','[NOMBRE]',regex=True)
    return s_low

def split_long_text(text,max_words=30):
    if not isinstance(text,str): return [text]
    words=text.split()
    if len(words)<=max_words: return [text]
    mid=len(words)//2
    return [' '.join(words[:mid]),' '.join(words[mid:])]

def main():
    df_raw = ensure_raw_dataset()
    relevantes=['id','fecha','idioma','categoria','producto','canal','asunto','texto','prioridad','estado']
    df = df_raw[relevantes].copy()
    df=df[df['categoria'].isin(['soporte','producto']) & (df['idioma']=='es')]
    df=df[~df['texto'].isna()]
    df=df[df['texto'].str.strip().str.len()>0]
    for col in ['producto','canal','prioridad','asunto','estado']:
        df[col]=df[col].fillna('desconocido')
    df['texto']=normalize_spaces_punct(df['texto'])
    df=df.drop_duplicates(subset=['texto','producto','asunto'],keep='first')
    df['texto']=df['texto'].apply(mask_pii)
    for col in ['texto','producto','asunto','canal','prioridad','estado']:
        df[col]=lowercase_preserve_tags(df[col].astype(str))
    df=df.assign(text_chunks=df['texto'].apply(split_long_text)).explode('text_chunks').drop(columns=['texto']).rename(columns={'text_chunks':'texto'}).reset_index(drop=True)
    df.to_excel(CLEAN_PATH_XLSX, index=False)
    try:
        df.to_parquet(CLEAN_PATH_PARQUET, index=False)
        print('Guardado Parquet:', str(CLEAN_PATH_PARQUET))
    except Exception as e:
        print('Parquet no disponible:', e)
    print('OK ->', str(CLEAN_PATH_XLSX))

if __name__=='__main__':
    main()
