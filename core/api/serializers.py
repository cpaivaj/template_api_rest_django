from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico, Atracao#, DocIdentificacao
from enderecos.models import Endereco
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
	# NestedRelationShip Carrega os objetos internos
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    #doc_identificacao

    class Meta:
        model = PontoTuristico
        fields = [
        	'id', 'nome', 'descricao', 'aprovado', 'foto',
        	'atracoes', 'comentarios', 'avaliacoes', 'endereco',
        	'descricao_completa', 'descricao_completa2'
        ]
        read_only_fields = ('comentarios', 'avaliacoes')

    # Salvando requests com objetos relacionados
    # Modelo ManyToMany
    # Objetos secundarios
    def cria_atracoes(self, atracoes, ponto):
    	for atracao in atracoes:
    		at = Atracao.objects.create(**atracao)
    		ponto.atracoes.add(at)

   	# Cria o registro principal e faz a chamada para inserir os objs secundarios
    def create(self, validated_data):
    	atracoes = validated_data['atracoes']
    	del validated_data['atracoes']

    	print(validated_data)

    	endereco = validated_data['endereco']
    	del validated_data['endereco']

    	#doc = validated_data['doc_identificacao']
    	#del validated_data['doc_identificacao']
    	#doci = DocIdentificacao.objects.create(**doc)

    	ponto = PontoTuristico.objects.create(**validated_data)
    	self.cria_atracoes(atracoes, ponto)

    	end = Endereco.objects.create(**endereco)
    	ponto.endereco = end
    	#ponto.doc_identificacao = doci

    	ponto.save()

    	return ponto


    # Funciona como um 'transient' (para nao precisar gravar isso no banco)
    def get_descricao_completa(self, obj):
    	return '%s - %s' % (obj.nome, obj.descricao)