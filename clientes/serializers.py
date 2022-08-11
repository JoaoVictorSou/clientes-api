from rest_framework import serializers
from clientes.models import Cliente
from .validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    """
    Neste formato:
    def validate_celular(self, celular):
        if not len(celular) >= 11:
            raise  serializers.ValidationError("O celular deve ter no mínimo 11 dígitos")
        else:
            return celular
    O Django desobre o campo a ser validado pelo validate_CELULAR
    """

    # Neste formato será passado todos os campos
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf":"CPF inválido!"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg":"RG deve conter extamente 9 dígitos!"})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome":"Um nome de pessoa deve conter apenas letras!"})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular":"O número deve estar no padrão DD NNNNN-NNNN"})
        
        return data
    