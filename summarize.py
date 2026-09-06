import os 
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
def summarize_text(context: str,transcript:str)-> str:
    prompt= f"""You are given a meeting transcript and optional context.
Context:{context if context else 'No additional context provided.'}
Transcript:{transcript}
Respond in exactly this format, with the exact section headers:
SUMMARY:
(3-5 key points, numbered)
ACTION ITEMS:
(list who needs to do what, numbered. If none, write "None Mentioned")
DECISIONS:
(list key decisions made, in the order they happened, numbered.If none, write "None Mentioned")
TONE:
(one short sentence describing the overall tone/sentiment of the meeting)
FOLLOW-UP EMAIL:
(a short professional follow-up email summarizing the meeting,written as if sent by the organizer to attendees)
"""
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":prompt}],
    )
    return response.choices[0].message.content
if __name__=="__main__":
    print("Step 1:Sending test transcript to Groq...")
    result=summarize_text("","This is a test transcript about a team discussing project deadlines nd deciding to push the launch by two weeks.")
    print("Step 2:Summary received!")
    print("Summary:", result)