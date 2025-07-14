import os
import httpx
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ✅ Create a standard HTTP client without passing 'proxies'
http_client = httpx.Client()  # omit proxies altogether

# ✅ Initialize the OpenAI-compatible Groq client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    http_client=http_client
)

def analyze_user_data_with_llm(user_data):
    analysis = {
        "motivations": [],
        "frustrations": [],
        "personality": [],
        "habits": [],
        "goals": [],
        "citations": []
    }

    prompt_template = """
Analyze the following Reddit {type} to extract any insights about the user's motivations, personality traits, frustrations, habits, or goals:
---
{text}
---
Reply in the format:
Motivations:
Frustrations:
Personality:
Habits:
Goals:
"""

    def call_groq(text, post_type):
        prompt = prompt_template.format(type=post_type, text=text)
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes Reddit data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    for post in user_data.get("posts", []):
        combined = post.get("title", "") + "\n" + post.get("selftext", "")
        if combined.strip():
            result = call_groq(combined, "post")
            analysis["citations"].append({"url": post["url"], "analysis": result})

    for comment in user_data.get("comments", []):
        body = comment.get("body", "")
        if body.strip():
            result = call_groq(body, "comment")
            analysis["citations"].append({"url": comment["url"], "analysis": result})

    return analysis
