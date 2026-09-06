from flask import Flask,request, render_template
from transcribe import transcribe_audio
from summarize import summarize_text 
import os
import re

app= Flask(__name__)
def parse_sections(text):
    sections={"SUMMARY":[],"ACTION ITEMS":[],"DECISIONS":[],"TONE":"","FOLLOW-UP EMAIL":""}
    current=None
    for line in text.split("\n"):
        line=line.strip()
        if not line:
            continue
        upper =line.upper().replace("#","").replace("*","").replace(":","").strip()
        if upper.startswith("SUMMARY"):
            current="SUMMARY"
            continue
        elif upper.startswith("ACTION ITEMS"):
            current="ACTION ITEMS"
            continue
        elif upper.startswith("DECISIONS"):
            current="DECISIONS"
            continue
        elif upper.startswith("TONE"):
            current="TONE"
            continue
        elif upper.startswith("FOLLOW-UP EMAIL") or upper.startswith("FOLLOW UP EMAIL"):
            current="FOLLOW-UP EMAIL" 
            continue
        clean_line=re.sub(r'^\d+\.\s*','',line)
        if current in("SUMMARY","ACTION ITEMS", "DECISIONS"):
            sections[current].append(clean_line)
        elif current in ("TONE", "FOLLOW-UP EMAIL"):
            sections[current]+=clean_line+""
    return sections        

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    audio_file=request.files["audio_file"]
    context= request.form.get("context","")
    os.makedirs("uploads", exist_ok=True)
    save_path=os.path.join("uploads", audio_file.filename)
    audio_file.save(save_path)
    transcript=transcribe_audio(save_path)
    summary=summarize_text(context, transcript)
    points= re.split(r'\d+\.\s*',summary)
    points=[p.strip() for p in points if p.strip()]
    sections=parse_sections(summary)

    return render_template("results.html",sections=sections,transcript=transcript)
if __name__=="__main__":
    app.run(debug=True)