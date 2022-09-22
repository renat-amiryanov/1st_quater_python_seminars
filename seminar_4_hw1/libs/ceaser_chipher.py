alphabet_ru = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя'
alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alphabet_symbols = ',./-*/!@#$%^&*()_+=-| '


def encrypt(message, offset):
    enc_message = ''

    for ch in message:
        if ch in alphabet_ru:
            pos = alphabet_ru.index(ch)
            enc_message += alphabet_ru[(pos + offset) % len(alphabet_ru)]
        elif ch in alphabet_en:
            pos = alphabet_en.index(ch)
            enc_message += alphabet_en[(pos + offset) % len(alphabet_en)]
        elif ch in alphabet_symbols:
            pos = alphabet_symbols.index(ch)
            enc_message += alphabet_symbols[(pos + offset) % len(alphabet_symbols)]
    return enc_message


def decrypt(message, offset):
    dec_message = ''
    for ch in message:
        if ch in alphabet_ru:
            pos = alphabet_ru.index(ch)
            dec_message += alphabet_ru[(pos - offset) % len(alphabet_ru)]

        elif ch in alphabet_en:
            pos = alphabet_en.index(ch)
            dec_message += alphabet_en[(pos - offset) % len(alphabet_en)]

        elif ch in alphabet_symbols:
            pos = alphabet_symbols.index(ch)
            dec_message += alphabet_symbols[(pos - offset) % len(alphabet_symbols)]

    return dec_message
