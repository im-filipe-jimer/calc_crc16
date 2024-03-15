def hex_to_bytes(hex_string):
    """
    Converte uma string hexadecimal em uma lista de bytes.
    
    Args:
        hex_string (str): A string hexadecimal.
    
    Returns:
        bytes_list (list): Lista de bytes.
    """
    bytes_list = []
    for i in range(0, len(hex_string), 2):
        bytes_list.append(int(hex_string[i:i+2], 16))
    return bytes_list

def xor_operation(bytes_list):
    """
    Realiza uma operação XOR nos bytes fornecidos.
    
    Args:
        bytes_list (list): Lista de bytes.
    
    Returns:
        result (int): Resultado da operação XOR.
    """
    result = bytes_list[0]
    for byte in bytes_list[1:]:
        result ^= byte
    return result

def crc16_operation(bytes_list):
    """
    Realiza uma operação CRC16 nos bytes fornecidos.
    
    Args:
        bytes_list (list): Lista de bytes.
    
    Returns:
        result (int): Resultado da operação CRC16.
    """
    crc = 0xFFFF
    polynomial = 0xA001

    for byte in bytes_list:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= polynomial
            else:
                crc >>= 1
    return crc


if __name__ == "__main__":
    # Exemplo de uso
    hex_string = "78783FA0"
    bytes_list = hex_to_bytes(hex_string)

    # Operação XOR
    xor_result = xor_operation(bytes_list)
    print("Resultado da operação XOR:", xor_result)

    # Operação CRC16
    crc16_result = crc16_operation(bytes_list)
    print("Resultado da operação CRC16:", crc16_result)
