import imp
import re
from validate_docbr import CPF

def cpf_valido(cpf):
    return CPF().validate(cpf)
    
def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    print(celular)
    padrao_celular = "[0-9]{2} [0-9]{5}[-][0-9]{4}"
    padrao_compilado = re.compile(padrao_celular)
    
    return padrao_compilado.match(celular)