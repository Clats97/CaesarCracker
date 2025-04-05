import string
import sys
import textwrap

try:
    import nltk
    from nltk.corpus import words
except ImportError:
    print("NLTK is required. Install it with 'pip install nltk' and run nltk.download('words').")
    sys.exit(1)

try:
    english_words_set = set(words.words())
except LookupError:
    nltk.download('words')
    english_words_set = set(words.words())

def print_header():
    red = "\033[31m"
    blue = "\033[34m"
    black = "\033[30m"
    reset = "\033[0m"
    ascii_art = """██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗         
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗        
██║     ███████║█████╗  ███████╗███████║██████╔╝        
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗        
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║        
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝         

 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"""
    header_text = "C A E S A R   C I P H E R   C R A C K E R"
    version_text = "Version 1.00"
    signature_text = "By Joshua M Clatney - Ethical Pentesting Enthusiast"
    print(red + ascii_art + reset)
    print(blue + header_text + " " + red + version_text + reset)
    print(black + signature_text + reset)

def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for ch in ciphertext:
        if ch.isalpha():
            if ch.isupper():
                decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += ch
    return decrypted

def is_english_sentence(text, threshold=0.75, min_words=2):
    tokens = text.split()
    if len(tokens) < min_words:
        return False
    valid_count = 0
    total_count = 0
    for token in tokens:
        cleaned = token.strip(string.punctuation).lower()
        if cleaned:
            total_count += 1
            if cleaned in english_words_set:
                valid_count += 1
    if total_count == 0:
        return False
    ratio = valid_count / total_count
    return ratio >= threshold

def main():
    while True:
        print_header()
        ciphertext = input("\nEnter the ciphertext (or press Enter to exit): ").strip()
        if ciphertext == "":
            sys.exit(0)
        found_valid = False
        for shift in range(26):
            decrypted_text = caesar_decrypt(ciphertext, shift)
            if is_english_sentence(decrypted_text):
                print("\nDecryption successful, valid English sentence found!")
                print("Shift: {}".format(shift))
                print("Decrypted text:")
                print("=" * 80)
                print(textwrap.fill(decrypted_text, 80))
                print("=" * 80)
                found_valid = True
                break
        if not found_valid:
            print("No valid English text was found for any shift.")
        input("\nPress Enter to return to the main screen...")

if __name__ == "__main__":
    main()