import os

print("=" * 60)
print("OSCILLOAI TRAINER DEBUG")
print("=" * 60)

files = [
    "config.py",
    "model.py",
    "callbacks.py",
    "train.py"
]

for file in files:

    print(f"\nChecking {file}")

    if os.path.exists(file):

        print("Status : FOUND")

        with open(file, "r", encoding="utf-8") as f:

            lines = f.readlines()

        print("-" * 40)

        for i, line in enumerate(lines, start=1):
            print(f"{i:03d}: {line.rstrip()}")

        print("-" * 40)

    else:

        print("Status : NOT FOUND")

print("\nDone.")