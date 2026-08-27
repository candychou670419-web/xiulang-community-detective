import os
import glob
import sys
import whisper

sys.stdout.reconfigure(encoding='utf-8')

print("Loading Whisper model...", flush=True)
model = whisper.load_model("tiny")

chunks = sorted(glob.glob("output/chunk_*.mp3"))
print(f"Found {len(chunks)} chunks to transcribe.", flush=True)

full_transcript = []

for idx, chunk in enumerate(chunks):
    start_min = idx * 5
    end_min = (idx + 1) * 5
    print(f"\n--- Transcribing Chunk {idx+1}/{len(chunks)} ({start_min:02d}:00 - {end_min:02d}:00) ---", flush=True)
    result = model.transcribe(chunk, language="zh", fp16=False)
    text = result.get("text", "").strip()
    print(f"Result [{idx+1}]: {text}", flush=True)
    full_transcript.append(f"【{start_min:02d}:00 - {end_min:02d}:00】\n{text}\n")

output_file = "output/transcript.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(full_transcript))

print(f"\nTranscription complete! Written to {output_file}", flush=True)
