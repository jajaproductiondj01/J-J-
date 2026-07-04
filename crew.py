import os
import re
import sys
from datetime import datetime

from crewai import Crew
from agents import grok, claude, gemini
from tasks import task1, task2, task3, task4

music_crew = Crew(
    agents=[grok, claude, gemini],
    tasks=[task1, task2, task3, task4],
    verbose=True
)


def slugify(text, max_words=6):
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())[:max_words]
    return "-".join(words) or "track"


def save_track(idea, timestamp):
    folder = os.path.join("tracks", f"{timestamp}_{slugify(idea)}")
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, "idea.txt"), "w") as f:
        f.write(idea + "\n")

    with open(os.path.join(folder, "01_structure.md"), "w") as f:
        f.write(task1.output.raw)

    with open(os.path.join(folder, "02_lyrics_enrichies.md"), "w") as f:
        f.write(task2.output.raw)

    with open(os.path.join(folder, "03_suno_prompt.md"), "w") as f:
        f.write(task3.output.raw)

    with open(os.path.join(folder, "04_mastering_notes.md"), "w") as f:
        f.write(task4.output.raw)

    return folder


if __name__ == "__main__":
    print("🚀 Système Multi-AI Music lancé !")
    idea = input("\nDécris ton idée de track : ")
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    result = music_crew.kickoff(inputs={"idea": idea})

    print("\n=== RÉSULTAT FINAL ===\n")
    print(result)

    folder = save_track(idea, timestamp)
    print(f"\n✅ Track sauvegardée dans : {folder}")
    print("👉 Copie le contenu de 03_suno_prompt.md sur suno.com, télécharge le mp3,")
    print(f"   place-le dans {folder}/, puis lance :")
    print(f"   python publish.py {folder}")
