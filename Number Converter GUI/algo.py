conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}


def decimalToHexa(decimal):
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


def decimalToBina(decimal):
    binary = 0
    ctr = 0
    temp = decimal  # copy input decimal

    # find binary value using while loop
    while temp > 0:
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1

    # output the result
    return binary


def BinaToDecimal(binary):
    dec_num = 0
    m = 1
    length = len(str(binary))

    for k in range(length):
        reminder = binary % 10
        dec_num = dec_num + (reminder * m)
        m = m * 2
        binary = int(binary / 10)

    return dec_num


def BinaToHexa(bina):
    a = BinaToDecimal(bina)
    return decimalToHexa(a)


def HexaToDecimal(hex):
    hex_to_dec_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    a = hex.strip().upper()
    dec = 0

    length = len(a) - 1

    for digit in a:
        dec += hex_to_dec_table[digit] * 16 ** length
        length -= 1

    return dec


def HexaToBina(Hexa):
    a = HexaToDecimal(Hexa)
    return decimalToBina(a)
