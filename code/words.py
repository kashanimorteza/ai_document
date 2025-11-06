import re
from collections import Counter

# -----------------------------
# Configuration
# -----------------------------
input_file = "/Volumes/data/documents/ai_document/readme.md"  # Path to your file
output_file = "words.txt"                                     # Output file

# -----------------------------
# Read and Extract Words
# -----------------------------
try:
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract only English words (4–14 letters)
    words = re.findall(r'\b[a-zA-Z]{4,14}\b', content)
    words = [w.lower() for w in words if w.isascii()]

    # Count word occurrences
    word_counter = Counter(words)

    # Save all words on one line
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(" ".join(word_counter.keys()))

    print(f"✅ Extracted {len(words)} words ({len(word_counter)} unique). Saved to {output_file}.")

    # -----------------------------
    # Show duplicate words
    # -----------------------------
    duplicates = {word: count for word, count in word_counter.items() if count > 1}
    if duplicates:
        print("\n🔁 Duplicate Words Found:")
        for word, count in sorted(duplicates.items(), key=lambda x: -x[1])[:20]:
            print(f"{word}: {count}")
    else:
        print("\n✅ No duplicate words found.")

except FileNotFoundError:
    print(f"❌ File not found: {input_file}")
except Exception as e:
    print(f"⚠️ Error: {e}")
