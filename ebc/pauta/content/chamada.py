# -*- coding: utf-8 -*-
"""Definition of the Chamada content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.ATVocabularyManager import NamedVocabulary
from Products.Archetypes.public import DisplayList

from Products.CMFCore.utils import getToolByName

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn
from collective.datagridcolumns.TextAreaColumn import TextAreaColumn

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import IChamada
from ebc.pauta.config import PROJECTNAME

ChamadaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-


    atapi.StringField(
        'episodio',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Episódio",
            description="Informe o nome, número ou data do episódio.",
        ),
    ),

    atapi.StringField(
        'fita_programa',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Fita do programa",
            description="Informe o número da fita do programa.",
        ),
    ),

    atapi.DateTimeField(
        'exibicao_programa',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label="Data de exibição do programa",
            description="Informe a data e a hora de exibição do programa.",
            format='%d/%m/%Y %H:%M',
            starting_year='2013',
        ),
        validators=('isValidDate'),
        required=True,
    ),

    DataGridField(
        name='chamada',
        columns=("roteiro", "validade", "fita"),
        widget=DataGridWidget(
            label=_(u"Chamadas"),
            columns={
                'roteiro': TextAreaColumn("Roteiro", rows="10", cols='50'),
                'validade': Column("Validade"),
                'fita': Column("Fita da chamada"),
            },
        ),
    ),

#    atapi.LinesField(
#        name='recebedor',
#        widget=atapi.InAndOutWidget(
#            label="Entregue para",
#        ),
#        vocabulary='getListaProgramacao',
#    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

ChamadaSchema['title'].storage = atapi.AnnotationStorage()
ChamadaSchema["title"].widget = atapi.SelectionWidget()
ChamadaSchema['title'].widget.label = "Programa"
ChamadaSchema['title'].vocabulary=NamedVocabulary("""programa""")
ChamadaSchema['description'].storage = atapi.AnnotationStorage()
ChamadaSchema['description'].widget.label = "Observações"
ChamadaSchema['description'].widget.description = ""



ChamadaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}
ChamadaSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}

ChamadaSchema.moveField('description', pos='bottom')

schemata.finalizeATCTSchema(
    ChamadaSchema,
    folderish=True,
    moveDiscussion=False
)

class Chamada(folder.ATFolder):
    """''"""
    implements(IChamada)

    meta_type = "Chamada"
    schema = ChamadaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    episodio = atapi.ATFieldProperty('episodio')
    fita_programa = atapi.ATFieldProperty('fita_programa')
    exibicao_programa = atapi.ATFieldProperty('exibicao_programa')
    recebedor = atapi.ATFieldProperty('recebedor')

    def getListaProgramacao(self):
        """ Retorna a lista de usuários do grupo programacao
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('Programacao')
        members = group.getGroupMembers()
        list = DisplayList()
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.add(memberId, fullname)
        return list


    def getStatusOff(self):
        """ Retorna a lista de status de Off
        """
        list = DisplayList()
        list.add('Nao','Não Precisa')
        list.add('Solicitado', 'Solicitado')
        list.add('EmProducao','Em produção')
        list.add('Pronto', 'Pronto')
        return list

    def getStatusCabeca(self):
        """ Retorna a lista de status de Cabecas
        """
        list = DisplayList()
        list.add('Nao','Não Precisa')
        list.add('Solicitado', 'Solicitado')
        list.add('EmProducao','Em produção')
        list.add('Pronto', 'Pronto')
        return list



atapi.registerType(Chamada, PROJECTNAME)
