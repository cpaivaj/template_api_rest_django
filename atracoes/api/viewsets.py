from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    ###### DJANGO FILTERS ######
    # pip install django-filters
    # Precisa add parametro no settings em instaled apps e ao final do arquivo settings
    filter_fields = ('nome', 'descricao')