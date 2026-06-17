# =========================
# 1. IMPORTS
# =========================
import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
col1, col2, col3 = st.columns([1,2,1])


# =========================
# 2. SETUP
# =========================
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="Bibel KI – Theologisches Tool",
    page_icon="📖",
    layout="wide"
)
st.markdown("""
<style>
/* Sidebar Hintergrund */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

/* Buttons dunkel machen */
.stButton > button {
    background-color: #1f2937 !important;
    color: #e5e7eb !important;
    border: 1px solid #374151 !important;
    border-radius: 8px;
}

/* Hover Effekt */
.stButton > button:hover {
    background-color: #334155 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
    background: linear-gradient(90deg, #d1d5db, #9ca3af);
    padding: 30px;
    border-radius: 15px;
    color: #111827;
    text-align: center;
    margin-bottom: 20px;
">
    <h1 style="margin:0;">📖 Bibel KI Studienzentrum</h1>
    <p style="margin:0; font-size:18px;">
        Exegese • Urtext • Theologie • Predigtvorbereitung
    </p>
</div>
""", unsafe_allow_html=True)
# =========================
# 3. DESIGN (UI GLOBAL)
# =========================
st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: #f3f4f6;
}

/* Sidebar Titel */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #111827;
}

/* Buttons */
.stButton > button {
    background-color: #374151 !important;
    color: white !important;
    border-radius: 8px;
    border: none;
}

/* Hover */
.stButton > button:hover {
    background-color: #10b981 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)
# =========================
# 4. HEADER
# =========================

# =========================
# 5. INPUT
# =========================
bibelstelle = st.text_input(
    "🔎 Bibelstelle eingeben",
    placeholder="z.B. Johannes 1:1"
)

# kombinierte Eingabe
full_input = bibelstelle

st.markdown("---")

# =========================
# 6. AI FUNCTION
# =========================
def run_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# =========================
# 7. OUTPUT FUNCTION (CLEAN UI)
# =========================
def render_result(result):
    st.markdown(f"""
    <div style="
        background-color: #111827;
        padding: 15px;
        border-radius: 12px;
        color: white;
        margin-top: 10px;
        white-space: pre-wrap;
    ">
    {result}
    </div>
    """, unsafe_allow_html=True)

# =========================
# 8. SIDEBAR ACTIONS
# =========================
col1, col2, col3 = st.sidebar.columns([1, 2, 1])

with col2:
    st.image("logo.jpg", width=90)

st.sidebar.title("Bibel KI Menü")



st.sidebar.markdown("-")

# =========================
# 📜 EXEGESE
# =========================
st.sidebar.markdown("### 📜 Exegese")

if st.sidebar.button("Urtext Analyse"):
    result = run_ai(f"""
Du bist ein Bibelwissenschaftler.

Analysiere den Urtext von:
{full_input}

Gib:
- griechische/hebräische Begriffe
- Grammatik
- semantische Bedeutung
- exegetische Interpretation
""")
    st.write(result)

if st.sidebar.button("Textkritik"):
    result = run_ai(f"""
Analysiere textkritische Aspekte:

{full_input}

- Varianten
- Manuskripte
- mögliche Unterschiede
""")
    st.write(result)

st.sidebar.markdown("-")

# =========================
# 🎙️ PREDIGT
# =========================
st.sidebar.markdown("### 🎙️ Predigt")

if st.sidebar.button("Predigt Ideen"):
    result = run_ai(f"""
Erstelle Predigtideen zu:

{full_input}

Struktur:
- Hauptbotschaft
- Illustration
- Anwendung
""")
    st.write(result)

if st.sidebar.button("Illustrationen"):
    result = run_ai(f"""
Gib praktische Illustrationen zu:

{full_input}
""")
    st.write(result)

st.sidebar.markdown("-")

# =========================
# 📚 STUDIUM
# =========================
st.sidebar.markdown("### 📚 Studium")

if st.sidebar.button("Fragen"):
    result = run_ai(f"""
Stelle 3 theologische Reflexionsfragen zu:

{full_input}
""")
    st.write(result)

if st.sidebar.button("Quiz"):
    result = run_ai(f"""
Erstelle ein theologisches Quiz:

{full_input}
""")
    st.write(result)

# =========================
# 9. EMPTY STATE
# =========================
else:
    st.info("Bitte eine Bibelstelle eingeben, um die Analyse zu starten.")