"""
Задача 4.
Шифр Цезаря - способ шифрования где каждая бука смещается на определенно количество
символов влево или вправо. При расшифровке происходит обратная операция.
К примеру, слово "абба"  можно зашифровать "бааб" - сдвиг на 1 вправо, "вггв" -  сдвиг на вправо 2
Написать функцию которая записывает в файл шифрованный текст, а так же функцию которая спрашивает ключ,
считывает текст и дешивровывает его.
"""
from matplotlib.pyplot import text

# alphabet = '1йфя2цыч3увс4кам5епи6нрт7гоь8шлб9щдю0зжхъ '
origin_text = 'считывает текст и дешивровывает его.'
encrypted_text = None
key = 4


def enccrypt(text, k):
    alphabet = '1йфя2цыч3увс4кам5епи6нрт7гоь8шлб9щдю0зжхъ.,?!ЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛБЩДЮЗЖХЭЪ"- '
    enc_string = ''
    text = text.replace('\n','')
    for t in text:
        orig_pos = alphabet.index(t)
        enc_pos = orig_pos + k
        if enc_pos >= len(alphabet):
            enc_pos = 0
        enc_string += alphabet[enc_pos]
    print('[+] Encryption done!')
    return enc_string

def decrypt(text, k):
    alphabet = '1йфя2цыч3увс4кам5епи6нрт7гоь8шлб9щдю0зжхъ.,?!ЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛБЩДЮЗЖХЭЪ"- '
    dec_string = ''
    text = text.replace('\n','')
    try:
        for t in text:
            orig_pos = alphabet.index(t)
            dec_pos = orig_pos - k
            if dec_pos <= 0:
                dec_pos = len(alphabet)-1
            dec_string += alphabet[dec_pos]
    except:
        print('[-] Decryption failed!')
    print('[+] Decryption done!')
    return dec_string

encrypted_text = enccrypt(origin_text,key)
print(origin_text, encrypted_text)
decrypted_text = decrypt(encrypted_text,key)
print(encrypted_text, decrypted_text)

