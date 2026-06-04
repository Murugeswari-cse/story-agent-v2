import json, random, sys, urllib.request
from config import GROQ_API_KEY
from mail_manager import send_story_to_gmail

topics = [
    "The sacrifice of a Freedom Fighter", "A brave soldier in the War field", 
    "An accidental Science discovery", "How AI/Technology changed a village", 
    "A young leader who united everyone", "A kid who built a sustainable future", 
    "The true value of Education", "A self-disciplined student's success", 
    "Planting trees to save a drying river", "Honesty in a difficult situation", 
    "Overcoming the fear of failure", "The power of unexpected kindness", 
    "Time management vs last-minute rush", "Why greed always leads to loss", 
    "The joy of sharing things with others"
]

def generate_story(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {'Authorization': f'Bearer {GROQ_API_KEY}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
    
    # Prompt with 150 words and one sentence moral
    full_prompt = f"Write a creative story about: {prompt}. \n\nRULES: \n1. Keep it around 150 words. \n2. Start with a Bold Heading. \n3. End with 'Moral:' followed by ONLY ONE simple sentence."
    
    payload = {"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": full_prompt}], "temperature": 0.7}
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode('utf-8'))
        return data['choices'][0]['message']['content']

while True:
    print("\n" + "="*30 + "\n 📖 STORY AGENT V2 \n" + "="*30)
    print(" 1. Random Story\n 2. Choose from 15 Topics\n 3. Context Based\n 4. Exit")
    choice = input("Select (1-4): ")
    
    if choice == "4": break
    
    prompt = ""
    if choice == "1":
        prompt = random.choice(topics)
    elif choice == "2":
        for i, t in enumerate(topics, 1): print(f"{i}. {t}")
        prompt = topics[int(input("Select Topic No (1-15): "))-1]
    elif choice == "3":
        prompt = input("Enter your context: ")
    else: continue

    print("\n🚀 Writing your story...")
    story = generate_story(prompt)
    print("\n" + story + "\n")

    if input("Send email? (Y/N): ").upper() == 'Y':
        send_story_to_gmail(story)