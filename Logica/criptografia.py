# -*- coding: utf-8 -*-
import random

def gerar_chave():
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
    chave = ''
    for _ in range(32):
        chave += letter[random.randint(0, len(letter) - 1)]
    return chave

def criptografar_senha(senha, chave):
    seed_user = sum(ord(c) for c in chave)
    
    def gerar(seed, indice):
        random.seed(seed + indice)
        return random.randint(1, 255)
    
    temp = ''
    for i in range(len(senha)):
        hex_valor = hex(gerar(seed_user, ord(senha[i])))[2:]  # Remove o "0x"
        temp += hex_valor
    return temp

def verificar_senha(senha_digitada, senha_criptografada, chave):
    senha_criptografada_digitada = criptografar_senha(senha_digitada, chave)
    return senha_criptografada_digitada == senha_criptografada