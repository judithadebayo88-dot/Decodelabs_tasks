## Caesar Cipher

A simple Python implementation of the classic Caesar cipher. A substitution cipher that shifts each letter in a message by a fixed number of positions in the alphabet.

## About

This project encrypts and decrypts text using the Caesar cipher technique, one of the earliest and simplest encryption methods. It was built as a hands-on way to understand basic cryptographic concepts like shift-based substitution and key handling.

## Features

- Encrypt plaintext into ciphertext using a chosen shift key
- Decrypt ciphertext back into plaintext using the same key
- Preserves case (uppercase/lowercase) and leaves non-alphabetic characters (spaces, punctuation, numbers) unchanged

## How It Works

Each letter in the input is shifted forward (encryption) or backward (decryption) by the key value, wrapping around the alphabet as needed (e.g., with a shift of 3, `A` becomes `D`, and `Z` wraps around to `C`).

## Requirements

- Python 3.x

## Usage

```bash
python ceaser-cipher.py
```

You'll be prompted to:
1. Enter the message
2. Enter a shift key (an integer)
3. Choose whether to encrypt or decrypt

### Example

```
Enter message: WELCOME
Enter shift key: 3
Encrypt or Decrypt? (e/d): e

Encrypted message: ZHOFRPH
```


