import streamlit as st
import os

# Inject custom CSS to increase font size
st.markdown(
    """
    <style>
    html, body, [class^='css']  {
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define topics and corresponding markdown files
TOPICS = [
    "Droit",
    "Économie",
    "Géographie",
    "Histoire",
    "Mathématiques",
    "Philosophie",
    "Psychologie"
]

HEADERS = {
    "Droit": "**Le droit face aux enjeux de la transition écologique : fondements, évolutions et perspectives**",
    "Économie": "**L'économie à l'épreuve de la transition écologique : fondamentaux, outils et enjeux pour l'enseignement supérieur**",
    "Géographie": "**Géographie et transition écologique : enjeux, échelles et stratégies**",
    "Histoire": "**L'histoire au cœur de la transition écologique : enjeux, méthodes et perspectives**",
    "Mathématiques": "**Mathématiques et transition écologique : enjeux, modélisation et perspectives**",
    "Philosophie": "**Philosophie et transition écologique : enjeux épistémologiques et éthiques**",
    "Psychologie": "**Psychologie et transition écologique : enjeux, mécanismes et perspectives pédagogiques**",
}

MD_DIR = "md"

def load_markdown(topic):
    md_path = os.path.join(MD_DIR, f"Microlearning - {topic}.md")
    if not os.path.exists(md_path):
        return "# Not found", "", ""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Split content at Bibliography section
    biblio_header = "## Bibliographie"
    welearn_header = "### Ressources complémentaires (via WeLearn)"
    main = content
    bibliography = ""
    welearn = ""
    if biblio_header in content:
        main, biblio = content.split(biblio_header, 1)
        bibliography = biblio.strip()
        # Try to extract WeLearn section from bibliography
        if welearn_header in bibliography:
            biblio_main, welearn = bibliography.split(welearn_header, 1)
            bibliography = biblio_main.strip()
            welearn = welearn.strip()
    return main, bibliography, welearn

def main():
    #st.set_page_config(layout="wide")
    st.title("Microlearning - Impacts et apports croisée des disciplines face à la TEDS")
    topic = st.selectbox("Choisissez un sujet :", TOPICS)
    if topic:
        main_content, bibliography, welearn = load_markdown(topic)
        st.header(HEADERS.get(topic, topic))
        tabs = ["Synthèse", "Bibliographie (UVED)", "Ressources complémentaires (WeLearn)"]
        selected_tab = st.tabs(tabs)
        with selected_tab[0]:
            st.markdown(main_content, unsafe_allow_html=True)
        with selected_tab[1]:
            if bibliography:
                st.header("Bibliographie (via UVED)")
                st.markdown(bibliography, unsafe_allow_html=False)
            else:
                st.info("Aucune bibliographie trouvée pour ce sujet.")
        with selected_tab[2]:
            if welearn:
                st.header("Ressources complémentaires (via WeLearn)")
                st.markdown(welearn, unsafe_allow_html=False)
            else:
                st.info("Aucune ressource complémentaire trouvée pour ce sujet.")

if __name__ == "__main__":
    main()
