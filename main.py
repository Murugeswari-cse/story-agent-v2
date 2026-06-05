import streamlit as st
import json, urllib.request, random
from mail_manager import send_story_to_gmail

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

topics = ["The sacrifice of a Freedom Fighter", "A brave soldier in the War field", "An accidental Science discovery", "How AI/Technology changed a village", "A young leader who united everyone", "A kid who built a sustainable future", "The true value of Education", "A self-disciplined student's success", "Planting trees to save a drying river", "Honesty in a difficult situation"]

def generate_story(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {'Authorization': f'Bearer {GROQ_API_KEY}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
    full_prompt = f"Write a creative story about: {prompt}. \n\nRULES: \n1. Keep it around 150 words. \n2. Start with a Bold Heading. \n3. End with 'Moral:' followed by ONLY ONE simple sentence."
    payload = {"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": full_prompt}], "temperature": 0.7}
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode('utf-8'))
        return data['choices'][0]['message']['content']

st.title("📖 STORY AGENT V2")
choice = st.selectbox("Select Mode", ["Random Story", "Choose from Topics", "Context Based"])

prompt = ""
if choice == "Random Story":
    prompt = random.choice(topics)
elif choice == "Choose from Topics":
    prompt = st.selectbox("Select Topic", topics)
elif choice == "Context Based":
    prompt = st.text_input("Enter your context:")

if st.button("Generate Story"):
    if prompt:
        with st.spinner("🚀 Writing..."):
            story = generate_story(prompt)
            st.markdown(story)
            st.session_state['last_story'] = story

if 'last_story' in st.session_state:
    if st.button("📧 Send Story to Email"):
        with st.spinner("Sending..."):
            if send_story_to_gmail(st.session_state['last_story']):
                st.success("✅ Email sent!")
            else:
                st.error("❌ Email failed!")