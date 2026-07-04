import subprocess
import sys
import os


def run(cmd):
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def main():
    if len(sys.argv) != 2:
        print("Usage: python publish.py <tracks/<dossier>>")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"Dossier introuvable : {folder}")
        sys.exit(1)

    track_name = os.path.basename(folder.rstrip("/"))

    run(["git", "add", folder])
    run(["git", "commit", "-m", f"Add track: {track_name}"])
    run(["git", "push", "origin", "main"])
    print(f"\n✅ Track '{track_name}' publiée sur GitHub.")


if __name__ == "__main__":
    main()
