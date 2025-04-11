# CaesarCracker
This Python script is designed to decrypt ciphertexts encrypted with the Caesar cipher. It tries all 26 possible shifts to find the one that produces a valid English sentence. It uses the Natural Language Toolkit to verify the decrypted text by checking if it contains sufficient valid English words.

# Caesar Cipher Cracker

## Key Features

- **ASCII Art Header:**  
  Displays a colorful ASCII art header that includes the tool's name, version, and the author’s signature.

- **Caesar Cipher Decryption:**  
  The `caesar_decrypt` function shifts each alphabetic character in the ciphertext backward by a specified number (shift), while preserving the letter's case. Non-alphabet characters remain unchanged.

- **English Sentence Verification:**  
  The `is_english_sentence` function splits the decrypted text into tokens, cleans punctuation, and compares the words against an English dictionary (provided by NLTK). A valid decryption is identified if the ratio of recognized English words meets or exceeds a threshold (default is 75%).

- **Brute-Force Approach:**  
  The script tries every possible shift from 0 to 25. If a decryption yields a valid English sentence, it displays the corresponding shift and decrypted text.

- **Interactive Interface:**  
  The script runs in a loop, prompting the user for ciphertext until an empty input is entered to exit.

## Prerequisites

- **Python 3.x**

- **NLTK (Natural Language Toolkit):**  
  Install NLTK via pip:
  
  pip install nltk

  **Author**
Joshua M Clatney (Clats97)
Ethical Pentesting Enthusiast

Copyright 2025 Joshua M Clatney (Clats97)

