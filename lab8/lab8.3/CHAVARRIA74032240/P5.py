def is_consonant(ch):
    ch = ch.lower()
    return ch.isalpha() and ch not in "aeiou"

def count_consonants_recursive(s, idx=0):
    if idx >= len(s):
        return 0
    add = 1 if is_consonant(s[idx]) else 0
    return add + count_consonants_recursive(s, idx + 1)

if __name__ == "__main__":
    texto = "Hola como estas Carlos"
    print("Cadena:", texto)
    print("Cantidad de consonantes:", count_consonants_recursive(texto))
