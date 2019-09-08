from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
	# NestedRelationShip Carrega os objetos internos
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = [
        	'id', 'nome', 'descricao', 'aprovado', 'foto',
        	'atracoes', 'comentarios', 'avaliacoes', 'endereco',
        	'descricao_completa', 'descricao_completa2'
        ]    

    # Funciona como um 'transient' (para nao precisar gravar isso no banco)
    def get_descricao_completa(self, obj):
    	return '%s - %s' % (obj.nome, obj.descricao)