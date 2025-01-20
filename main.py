import streamlit as st

def menu():
    pages = {
        "CREATE": [
            st.Page("views/1_texttospeech.py", title="Text to Speech", icon=":material/font_download:"),
            st.Page("views/2_voicechanger.py", title="Voice Changer", icon=":material/record_voice_over:"),
            st.Page("views/3_voices.py", title="Voices", icon=":material/graphic_eq:"),
            st.Page("views/4_soundeffects.py", title="Sound Effects", icon=":material/air:"),
            st.Page("views/14_Speech_to_text.py", title="Speech to Text", icon=":material/mic:"),
        ],
        "CONVERSATIONAL": [
            st.Page("views/5_agents.py", title="Agents", icon=":material/headset_mic:"),
        #     st.Page("views/6_conversations.py", title="Conversations", icon=":material/forum:"),
        #     st.Page("views/7_phonenumbers.py", title="Phone Numbers", icon=":material/call:"),
        ],
        # "WORKFLOWS": [
        #     st.Page("views/8_projects.py", title="Projects", icon=":material/collections_bookmark:"),
        #     st.Page("views/9_voiceover_studio.py", title="Voiceover Studio", icon=":material/radio:"),
        #     st.Page("views/10_dubbing_studio.py", title="Dubbing Studio", icon=":material/translate:"),
        #     st.Page("views/11_audio_native.py", title="Audio Native", icon=":material/volume_down:"),
        # ],
        # "TOOLS": [
        #     st.Page("views/12_voice_isolator.py", title="Voice Isolator", icon=":material/contactless:"),
        #     st.Page("views/13_ai_speech_classifier.py", title="AI Speech Classifier", icon=":material/branding_watermark:"),
        # ],
    }

    pg = st.navigation(pages)
    pg.run()

# Ensure the script only runs when directly imported and called
if __name__ == "__main__":
    menu()

