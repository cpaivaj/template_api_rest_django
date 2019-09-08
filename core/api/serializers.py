from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
	# NestedRelationShip Carrega os objetos internos
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = [
        	'id', 'nome', 'descricao', 'aprovado', 'foto',
        	'atracoes', 'comentarios', 'avaliacoes', 'endereco'
        ]