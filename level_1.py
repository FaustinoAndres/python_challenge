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

    message_modified = MESSAGE.replace(" ", "+")
    message_list = list(message_modified)

    message_unencoded_list = list()
    for char in message_list:
            message_unencoded_list.append(chr(ord(char) + 2))

    message_unencoded = "".join(message_unencoded_list).replace("-", " ")

    print(message_unencoded)



if __name__ == '__main__':
    main()
