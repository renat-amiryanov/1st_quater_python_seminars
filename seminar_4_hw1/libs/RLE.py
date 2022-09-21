
def compress(message):
    """
    Функция которая выполняет сжатие переданного текста
    :param message: Исходные текст который нужно сжать
    :return: Возврат сжатого текста
    """
    compressed_message = ''
    i = 0
    length = len(message)
    while i <= length - 1:
        count = 1
        j = i
        while j < length - 1:
            if message[i] == message[j + 1]:
                count += 1
                j += 1
            else:
                break
        compressed_message = compressed_message + str(count) + message[i]
        i = j + 1
    return compressed_message


def uncompress(message):
    uncompressed_message = ''
    i = 0
    length = len(message)
    while i <= length - 1:
        count = int(message[i])
        ch = str(message[i + 1])
        uncompressed_message += ch * count
        i += count-1
    return uncompressed_message
