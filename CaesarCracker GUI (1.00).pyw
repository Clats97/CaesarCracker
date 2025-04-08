import tkinter as tk
import tkinter.font as tkFont
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

def paste_clipboard_text():
    try:
        data = root.clipboard_get()
    except Exception:
        data = ""
    ciphertext_text.delete("1.0", tk.END)
    ciphertext_text.insert(tk.END, data)

def copy_to_clipboard():
    text = output_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text)
    
def clear_inputs():
    ciphertext_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

def gui_crack():
    output_text.delete("1.0", tk.END)
    ciphertext = ciphertext_text.get("1.0", tk.END).strip()
    if not ciphertext:
        output_text.insert(tk.END, "Please enter the ciphertext in the input field.\n")
        return
    output_text.insert(tk.END, "Ciphertext:\n" + "*" * 80 + "\n")
    output_text.insert(tk.END, textwrap.fill(ciphertext, 80) + "\n")
    output_text.insert(tk.END, "*" * 80 + "\n")
    found_valid = False
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        if is_english_sentence(decrypted_text):
            output_text.insert(tk.END, "\nDecryption successful, valid English sentence found!\n")
            output_text.insert(tk.END, "Shift: {} \n".format(shift))
            output_text.insert(tk.END, "Decrypted text:\n")
            output_text.insert(tk.END, "=" * 80 + "\n")
            output_text.insert(tk.END, textwrap.fill(decrypted_text, 80) + "\n")
            output_text.insert(tk.END, "=" * 80 + "\n")
            found_valid = True
            break
    if not found_valid:
        output_text.insert(tk.END, "No valid English text was found for any shift.\n")

root = tk.Tk()
root.title("Caesar Cipher Cracker GUI v1.00")
mono_font = tkFont.Font(family="Courier", size=10)
header_frame = tk.Frame(root)
header_frame.pack(fill=tk.X, padx=5, pady=5)
ascii_art = (
"     ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     \n"
"    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    \n"
"    ██║     ███████║█████╗  ███████╗███████║██████╔╝    \n"
"    ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    \n"
"    ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    \n"
"     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    \n"
"                                                        \n"
" ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ \n"
"██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗\n"
"██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝\n"
"██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗\n"
"╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║\n"
" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n"
"                                                        "
)
ascii_label = tk.Label(header_frame, text=ascii_art, fg="red", font=mono_font, justify="left")
ascii_label.pack(anchor="w")
title_frame = tk.Frame(header_frame)
title_frame.pack(anchor="w", pady=(2, 0))
title_text = "C A E S A R   C I P H E R   C R A C K E R"
title_label = tk.Label(title_frame, text=title_text, fg="blue", font=mono_font)
title_label.pack(side="left")
version_label = tk.Label(title_frame, text="  Version 1.00", fg="red", font=mono_font)
version_label.pack(side="left")
signature_text = "By Joshua M Clatney - Ethical Pentesting Enthusiast"
signature_label = tk.Label(header_frame, text=signature_text, fg="black", font=mono_font)
signature_label.pack(anchor="w", pady=(2, 5))
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=5, pady=5)
ciphertext_label = tk.Label(input_frame, text="Ciphertext:")
ciphertext_label.grid(row=0, column=0, sticky=tk.W, padx=2, pady=2)
ciphertext_frame = tk.Frame(input_frame)
ciphertext_frame.grid(row=1, column=0, columnspan=2, padx=2, pady=2, sticky="w")
ciphertext_text = tk.Text(ciphertext_frame, height=5, width=70, font=mono_font)
ciphertext_text.grid(row=0, column=0)
paste_button = tk.Button(ciphertext_frame, text="Paste", command=paste_clipboard_text)
paste_button.grid(row=0, column=1, padx=5)
crack_button = tk.Button(input_frame, text="Crack", command=gui_crack)
crack_button.grid(row=2, column=0, columnspan=2, pady=5)
output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
output_label = tk.Label(output_frame, text="Output:")
output_label.pack(anchor="w")
output_area_frame = tk.Frame(output_frame)
output_area_frame.pack(fill=tk.BOTH, expand=True)
output_text = tk.Text(output_area_frame, height=15, width=80, font=mono_font)
output_text.grid(row=0, column=0, sticky="nsew")
copy_button = tk.Button(output_area_frame, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=0, column=1, padx=5, sticky="n")
clear_button = tk.Button(output_area_frame, text="Clear", command=clear_inputs)
clear_button.grid(row=1, column=1, padx=5, pady=(5, 0), sticky="n")
output_area_frame.grid_rowconfigure(0, weight=1)
output_area_frame.grid_columnconfigure(0, weight=1)
root.mainloop()