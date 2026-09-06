# MeetScribe AI
MeetScribe AI is an AI-powered meeting assistant that converts meeting recordings into organized structured notes.

---
## About
MeetScribe AI helps users by:
- 🎙️ Converting meeting audio into text
- 📝 Creating a short summary
- ✅ Extracting action items
- 📌 Identifying key decisions
- 😊 Analyzing the meeting tone
- 📧 Generating a follow-up email

---
# Why I Built this
-Manual note-taking is time consuming.
-Important points can be missed during meetings.
-I wanted to build an AI solution that saves time.
-This project helped me apply AI concepts to solve a real-world problem.

---
## What makes MeetScribe AI different?
Unlike basic transcription tools,
MeetScribe AI:
-Doesn't just convert speech to text.
-Generates meaningful summaries.
-Finds action items automatically
-Highlights important decisions.
-Creates a professional follow-up email.
-Presents everything in a clean and simple interface.

---
## Features
- 🎙️ Upload WAV, MP3, or M4A audio files
- 📝 AI-generated meeting summary
- ✅ Automatic action items
- 📌 Key decisions
- 😊 Tone analysis
- 📧 Follow-up email generation
- 🎨 Modern and responsive UI

---
## Tech stack
### Front-end
- HTML
- CSS
- Javascript
### Back-end
- Python
- Flask
### AI Tools
- Whisper
- Google Gemini

---
## How it works
1.Upload--user selects an audio recording and optional context

2.Transcription--Faster-Whisper converts speech to text locally

3.Structured summarization--the transcript is sent to Groq's LLM with a structured prompt requesting summary,action items,decisions, tone,and a follow-up email in a consistent format.

4.Parsing--the response is parsed into distinct sections

5.Display--results are rendered on a clean,styled results page.

## Author
Rashmika.S
Third-year CS Engineering student,
Sathyabama Institute of Science and Technology
