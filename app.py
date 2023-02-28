import streamlit as st 
import time
from utils import recognize_from_microphone, generate_response
from speech import recognize

st.set_page_config(
    page_title='IA parle moi plus !',
    layout='wide',
    page_icon='🎤'
)

# !------------------------------------ CSS ------------------------------------!

st.markdown(
    """
    <style>
    
    div.stApp {
        background-image: url("https://codetheweb.blog/assets/img/posts/css-advanced-background-images/cover.jpg");
        background-size: cover;
        background-repeat: no-repeat;
    }
    
    div.stButton {
        margin-bottom: 2rem;
    }
    
    button.css-1x8cf1d  {
        margin: 0 auto;
        display: block;
        font-size: 24px;
        height: 60px;
        transition-duration: 0.5s;
    }
    
    button.css-1x8cf1d:hover {
        color: white;
        background-color: green;
    }
    
    p {
        font-size:2rem;
        font-weight: lighter;
        font-family: sans-serif;
    }

    div.css-zt5igj{
        color:black;
        display:flex;
        text-align:center;
        margin-bottom:5rem;
        font-weight: bold;
        font-family: "Gill Sans", sans-serif;
        font-size:3.5rem;
    }
    
    p.ia_container {
        color: white;
        background-color: transparent;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    
    div.stButton {
        display: flex;
        align-items:center;
        justify-content:center;
        animation: pulse 2s infinite;
    }
    
    button.css-629wbf{
        transition-duration: 0.5s;
        margin-top: 30rem;
    }
    
    button.css-629wbf:hover{
        color: white;
        background-color:red;
    }
    
    div.appview-container{
        background-image: url("openai-quickstart-python/img/fond.jpg");
        background-repeat: no-repeat;
        background-size:cover;
    }
    
    div.st-cg{
        font-size: 1.5rem;
    }
    
    div.st-bp{
        margin-top:12px;
    }
    
    div.css-184tjsw > p{
        font-size: 2rem;
        text-align:center;
        margin-bottom: 2rem;
    } 
    
    div.block-container{
        background-image: url("openai-quickstart-python/img/fond.jpg");
    }
    
    p.human_container{
        color: black;
        background-color: transparent;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
    """,
    unsafe_allow_html=True,
)

# !------------------------------------ FIN CSS ------------------------------------!

tchat_list = []

left_menu = st.sidebar
Play = True

with left_menu:
            choice = st.radio('Choose your recognition service', ('Azure service', 'Speech library'))
            if st.button("Ferme la ❌!!!"):
                st.snow()
                Play = False
                
st.header('IA parle moi plus 🤖!')

if st.button("Cliquez ici et parlez"):
    while Play == True:
        # Transcrit la parole en texte
        if choice == 'Azure service':
            speech_text, speech_voc = recognize_from_microphone()
            st.balloons()
            if not speech_text:
                continue
            
            
            human_container = st.empty()
            for i in range(len(speech_text)):
                human_container.markdown(f'<p class="human_container">{speech_text[:i+1]}</p>', unsafe_allow_html=True)
                time.sleep(0.01) 
                    
            # Génère une réponse à partir du texte transcrit
            response = generate_response(speech_text, tchat_list)

            # Affiche la réponse
            print(response)
            ia_container = st.empty()
            for i in range(len(response)):
                ia_container.markdown(f'<p class="ia_container">{response[:i+1]}</p>', unsafe_allow_html=True)
                time.sleep(0.01) 

            # Synthétise la réponse vocalement
            # Pour activer la synthèse vocale, enlevez la ligne en commentaire ci-dessous
            speech_voc.speak_text_async(response).get()
            
        elif choice == 'Speech library':
            speech_text, speech_voc = recognize()
            st.balloons()
            if not speech_text:
                continue
                    
            # Génère une réponse à partir du texte transcrit
            response = generate_response(speech_text, tchat_list)

            # Affiche la réponse
            print(response)
            ia_container = st.empty()
            for i in range(len(response)):
                ia_container.markdown(f'<p class="ia_container">{response[:i+1]}</p>', unsafe_allow_html=True)
                time.sleep(0.01)