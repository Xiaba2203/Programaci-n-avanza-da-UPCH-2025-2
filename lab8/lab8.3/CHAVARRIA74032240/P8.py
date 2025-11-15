def count_letter_recursive(s, letter, idx=0):
    if idx >= len(s):
        return 0
    add = 1 if s[idx].lower() == letter.lower() else 0
    return add + count_letter_recursive(s, letter, idx + 1)

if __name__ == "__main__":
    texto = "Hola como estas Carlos"
    letra = "o"
    print(f"En '{texto}' la letra '{letra}' aparece {count_letter_recursive(texto, letra)} veces.")
