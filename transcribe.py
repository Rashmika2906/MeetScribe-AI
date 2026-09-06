from faster_whisper import WhisperModel
print("Step 1:LOADING MODEL")
model=WhisperModel("base",device="cpu",compute_type="int8")
print("Step 2:MODEL LOADED")
def transcribe_audio(audio_path:str) ->str:
    print("Step3:STARTING TRANSCRIPTION")
    segments,info =model.transcribe(audio_path)
    full_text=""
    for segment in segments:
        full_text+= segment.text+""
    print("Step4:TRANSCRIPTON COMPLETE")
    return full_text.strip()
if __name__=="__main__":
    result=transcribe_audio("test_audio.wav")
    print("Transcribe result:",repr(result))