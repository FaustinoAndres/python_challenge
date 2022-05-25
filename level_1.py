def main():
    """
    Level 1:
        Solve http://www.pythonchallenge.com/pc/def/map.html
            everybody thinks twice before solving this.
        Hint:
            - Use the hints. They are helpful, most of the times.
            - Investigate the data given to you.
            - Avoid looking for spoilers.
    """

    url = "http://www.pythonchallenge.com/pc/def/map.html"

    MESSAGE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

    print(decrypt(MESSAGE))
    map_decrypt = decrypt('map')

    print(url.replace('map', map_decrypt))


def decrypt(message):

    start_abc = ord('a')
    end_abc = ord('z')

    module = end_abc - start_abc + 1
    message_list = list(message)

    message_decrypted_list = list()
    for char in message_list:
        if char.isalpha():
            new_char = chr(((ord(char) + 2 - start_abc) % module) + start_abc)
            message_decrypted_list.append(new_char)
        else:
            message_decrypted_list.append(char)

    message_decrypted = "".join(message_decrypted_list)

    return message_decrypted

if __name__ == '__main__':
    main()
