# -*- coding: utf-8 -*-
"""Definition of the evento content type
"""

from zope.interface import implements, directlyProvides

from DateTime.DateTime import *


from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.ATVocabularyManager import NamedVocabulary
from Products.Archetypes.public import DisplayList

from Products.CMFCore.utils import getToolByName

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import IEvento
from ebc.pauta.config import PROJECTNAME

EventoSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'obs_importante',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Observação importante",
        ),
    ),

    atapi.DateTimeField(
        'data_hora',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label="Data e hora do evento",
            description="Informe a data e a hora do evento.",
            format='%d/%m/%Y %H:%M',
            starting_year='2013',
        ),
        default_method = 'getDefaultTime',
        validators=('isValidDate'),
        required=True,
    ),

    atapi.StringField(
        'ordem_servico',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Ordem de Serviço",
            description="Informe o número da ordem de serviço.",
        ),
        searchable=True,
    ),

    atapi.LinesField(
        'tipo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label="Tipo da OS",
            description="Selecione o tipo da ordem de serviço.",
        ),
        required=False,
        vocabulary=NamedVocabulary("""TipoOS"""),
    ),

    atapi.LinesField(
        'politica',
        storage=atapi.AnnotationStorage(),
        widget=atapi.InAndOutWidget(
            label="Política pública",
            description="Selecione uma ou mais política pública.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""PoliticaPublica"""),
        required=True,
        searchable=True,
    ),

    atapi.LinesField(
        'ministerio',
        storage=atapi.AnnotationStorage(),
        widget=atapi.InAndOutWidget(
            label="Órgão",
            description="Selecione o órgão.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""Orgao"""),
        required=True,
        searchable=True,
    ),


    atapi.TextField(
        'local',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Local",
            description="Informe o local do evento",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
    ),

    atapi.TextField(
        'contatos',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Contatos",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
    ),

    atapi.TextField(
        'flashes',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Flashes",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
        
    ),

    atapi.TextField(
        'rodapes',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Rodapés",
            description="Informe os textos para o rodapé.",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
        
    ),

    atapi.TextField(
        'creditos',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Créditos",
            description="Informe os nomes e cargos para os créditos.",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
    ),

    atapi.TextField(
        'visita',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Visita técnica",
            description="Preencha o relatório da visita técnica.",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
    ),

    DataGridField(
        name='veiculacao',
        columns=("descricao", "entrada", "saida" ),
        widget=DataGridWidget(
            label="Veiculação",
            columns={
                'descricao': Column("Descricao"),
                'entrada':  Column("Entrada"),
                'saida':  Column("Saida"),
            },
        ),
        required=True,
    ),

    atapi.ComputedField(
        'duracao',
        expression='context.duracaoTotal()',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ComputedWidget(
            label="Duração da transmissão",
            modes=('view')
        ),
    ),

    atapi.TextField(
        'ocorrencias',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Ocorrências",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
    ),

    atapi.TextField(
        'observacoes',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Observações",
        ),
        allowable_content_types="('text/html')",
        default_output_type="text/html",
        searchable=1,
    ),

    atapi.LinesField(
        name='vcg',
        widget=atapi.SelectionWidget(
            label="Vocabulário Controlado",
            description="Selecione uma opção.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""vcg"""),
        required=True,
        searchable=True,
    ),

    atapi.LinesField(
        name='abrangencia',
        widget=atapi.InAndOutWidget(
            label="Abrangência",
            description="Selecione uma ou mais opções.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""abrangencia"""),
        required=True,
        searchable=True,
    ),


    atapi.LinesField(
        name='orgaoscitados',
        widget=atapi.InAndOutWidget(
            label="Orgãos citados",
            description="Selecione uma ou mais opções.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""orgaoscitados"""),
        searchable=True,
    ),


    atapi.LinesField(
        name='planos',
        widget=atapi.InAndOutWidget(
            label="Planos e programas citados",
            description="Selecione uma ou mais opções.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""planos"""),
        searchable=True,
    ),


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

EventoSchema['title'].widget.label = _(u"Evento")
EventoSchema['title'].storage = atapi.AnnotationStorage()
EventoSchema['description'].storage = atapi.AnnotationStorage()
EventoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}



schemata.finalizeATCTSchema(
    EventoSchema,
    folderish=True,
    moveDiscussion=False
)

class Evento(folder.ATFolder):
    """Description of the Example Type"""
    implements(IEvento)

    meta_type = "Evento"
    schema = EventoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    obs_importante = atapi.ATFieldProperty('obs_importante')
    data_hora = atapi.ATFieldProperty('data_hora')
    ordem_servico = atapi.ATFieldProperty('ordem_servico')
    tipo = atapi.ATFieldProperty('tipo')
    politica = atapi.ATFieldProperty('politica')
    local = atapi.ATFieldProperty('local')
    contatos = atapi.ATFieldProperty('contatos')
    flashes = atapi.ATFieldProperty('flashes')
    rodapes = atapi.ATFieldProperty('rodapes')
    creditos = atapi.ATFieldProperty('creditos')
    visita = atapi.ATFieldProperty('visita')
    ocorrencias = atapi.ATFieldProperty('ocorrencias')
    observacoes = atapi.ATFieldProperty('observacoes')

    def getDefaultTime(self):
        return DateTime()

    def duracaoTotal(self):
        veiculacoes = self.getVeiculacao()
        duracao = 0

        for veiculacao in veiculacoes:
            entrada = veiculacao['entrada'].split(':')
            saida = veiculacao['saida'].split(':')
            entrada_h = int(entrada[0])
            entrada_m = int(entrada[1])
            saida_h = int(saida[0])
            saida_m = int(saida[1])

            # Entrada menor que saída
            min_entrada = 60 * entrada_h + entrada_m
            min_saida = 60 * saida_h + saida_m

            if min_entrada < min_saida:
                duracao = duracao + min_saida - min_entrada
            else:
                duracao = duracao + (1440 - min_entrada) + min_saida

        return str(duracao) + ' minutos'


    def start(self):
        return self.getData_hora()

    def end(self):
        return self.getData_hora()


atapi.registerType(Evento, PROJECTNAME)
