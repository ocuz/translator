#!/usr/bin/env python3

from googletrans import Translator
import time
import sys

def translate_words_file(input_file, output_file, delay=0.1):
    translator = Translator()
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            words = [line.strip() for line in infile if line.strip()]
        
        translated_words = []
        for i, word in enumerate(words, 1):
            try:
                translation = translator.translate(word, src='en', dest='fr') #en and fr are the language codes change to whatever to translate from one to other
                translated_words.append(translation.text)
                print(f"({i}/{len(words)}) {word} -> {translation.text}")
                time.sleep(delay)
            except Exception as e:
                print(f"Error translating '{word}': {e}")
                translated_words.append(word)
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for word in translated_words:
                outfile.write(word + '\n')
        
        print(f"Done. Saved to '{output_file}'")
        
    except FileNotFoundError:
        print(f"File not found: '{input_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_filename = "e_w.txt"
    output_filename = "f_w.txt"
    
    if len(sys.argv) >= 2:
        input_filename = sys.argv[1]
    if len(sys.argv) >= 3:
        output_filename = sys.argv[2]
    
    print(f"Translating '{input_filename}' -> '{output_filename}'")
    translate_words_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
