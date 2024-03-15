# -*- coding: utf-8 -*-
# Data: 2023-01-20 14:39
# Author: Matheus Eudes
# Refactored: 2024-03-01 11:40
# by: Filipe Ferreira

# Função para calcular o checksum de uma lista de bytes

def calc_checksum(data: list, _int: bool = False) -> str|int:
	"""Calcula o checksum de uma lista de bytes
	:param data: lista de bytes
	:return: checksum

	>>> calc_checksum([0x0a,0x00,0x2b,0xce,0x16], False)
	>>> '0xf9'
	>>> calc_checksum([0x0a,0x00,0x2b,0xce,0x16], True)
	>>> 249
	"""
	checksum = 0
	for byte in data:
		checksum ^= byte
	if _int:
		return checksum
	else:
		return hex(checksum)


if __name__ == "__main__":
	calc_checksum([0x0a,0x00,0x2b,0xce,0x16], True)
