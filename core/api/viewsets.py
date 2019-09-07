from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

# O modelViewSet ja tem o CRUD disponivel - AWESOME
class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    """
    Sobrescreve o metodo
    Aqui dentro podem haver varios filtros
    Quando usa dessa forma, precisa colocar o base_name na url dentro do urls.py na pasta principal(pontos_turisticos)
    Esse metodo sempre precisa retornar um iterable (lista de queryset)
    """
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    """
    Sobrescrita do metodo 'list', esse metodo eh chamado sempre que for usado o GET sem parametro, para trazer 'tudo'
    Com essa sobrescrita eh possivel personalizar o retorno do GET
    """
    #def list(self, request, *args, **kwargs):
    #    return Response({'teste':123})

    """
    Sobrescrita do metodo 'create', que eh chamado atraves do POST
    """
    #def create(self, request, *args, **kwargs):
    #    return Response({'Hello': request.data['nome']})

    """
    Sobrescreve o metodo 'destroy', que eh chamado atraves do DELETE
    Precisa do ID a ser deletado
    Nessa sobrescrita pode colocar permissoes, salvar historico de quem apagou, dentre outras caracteristicas
    """
    #def destroy(self, request, *args, **kwargs):
    #    pass

    """
    Sobrescreve o 'retrieve', esse metodo eh chamado quando usa o GET com algum parametro, buscar informacoes especificas
    Exemplo: pontosturisticos/1/
    """
    #def retrieve(self, request, *args, **kwargs):
    #    pass

    """
    Chamado atraves do PUT
    Atualiza o registro todo (precisa de todos os parametros)
    """
    #def update(self, request, *args, **kwargs):
    #    pass

    """
    Chamada atraves do PATCH
    Pode atualizar um campo apenas (nao precisa passar todos os valores do registro)
    """
    #def partial_update(self, request, *args, **kwargs):
    #    pass

    """
    ***** ACTIONS PERSONALIZADAS *****
    
    A annotation @action serve pra indicar que eh uma action personalizada
    O campo methods indica quais metodos HTTP poderao ser usados para fazer a chamada dessa action nova
    O campo detail=True faz com que a pk seja usada, se passar False, nao usa pk entao busca tudo assim como o list, sem a pk nao tem jeito de fazer as operacoes necessarias em um determinado registro
    Por causa do datail=True, eh necessario passar uma pk para que este metodo seja chamado
    Exemplo: pontosturisticos/1/denunciar/
    """
    #@action(methods=['get'], detail=True)
    #def denunciar(self, request, pk=None):
    #    pass

    # @action(methods=['get'], detail=False)
    # def busca_tudo(self, request):
    #    pass