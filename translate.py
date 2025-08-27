from deep_translator import GoogleTranslator
import sys, time

def translate_file(input_file, output_file, batch_size=50, delay=0.3):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            words = [w.strip() for w in f if w.strip()]
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found."); return

    print(f"Found {len(words)} words translating in batches of {batch_size}...")
    translator = GoogleTranslator(source="en", target="fr")
    translations = []

    for i in range(0, len(words), batch_size):
        batch = words[i:i+batch_size]
        try:
            translated = translator.translate_batch(batch)
            translations.extend(translated)
            print(f"Batch {i//batch_size+1}: {batch[0]} → {translated[0]} ...")
        except Exception as e:
            print(f"Batch {i//batch_size+1} failed: {e}. Retrying individually...")
            for w in batch:
                try:
                    translations.append(translator.translate(w))
                except: 
                    translations.append(w)
                time.sleep(0.1)
        time.sleep(delay)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(translations))
    print(f"saved {len(translations)} translations to '{output_file}'")

def main():
    input_file  = sys.argv[1] if len(sys.argv) > 1 else "english_words.txt"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "french_words.txt"
    batch_size  = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    translate_file(input_file, output_file, batch_size)

if __name__ == "__main__":
    main()
