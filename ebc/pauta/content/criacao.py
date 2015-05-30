# -*- coding: utf-8 -*-
"""Definition of the Criacao content type
"""

from zope.interface import implements, directlyProvides
import datetime
from DateTime import DateTime

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.utils import dt2DT

from Products.Archetypes.public import DisplayList
from Products.CMFCore.utils import getToolByName

from Products.validation.validators.ExpressionValidator import ExpressionValidator

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import ICriacao
from ebc.pauta.config import PROJECTNAME

CriacaoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.StringField(
        'solicitante',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Nome do solicitante",
            description="Informe o nome da pessoa que fez a solicitação.",
        ),
    ),

    atapi.StringField(
        'orgao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Informe o órgão/setor do solicitante",
            description="Informe órgão/setor da pessoa que fez a solicitação.",
        ),
    ),

    atapi.StringField(
        'contato',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Informações de contato",
            description="Preencha com informações de contato.",
        ),
    ),

    atapi.DateTimeField(
       name='data',
       default_method=DateTime,       
       widget=atapi.CalendarWidget(
           label="Data da solicitação",
           show_hm=False,
           format='%d/%m/%Y',
           starting_year='2014',           
       ),
    ),

    atapi.LinesField(
        name='tipo',
        widget=atapi.SelectionWidget(
            label="Tipo da solicitação",
            description="Selecione o tipo da solicitação.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""tipoSolicitacao"""),
        required=True,
        searchable=True,
    ),

    atapi.TextField(
        name='descricao',
        widget=atapi.TextAreaWidget(
            label="Descrição",
            description="Descrição detalhada da solicitação.",            
        ),
    allowable_content_types="('text/html','text/plain')",
    default_output_type="text/html",
    searchable=1,
    ),

    atapi.DateTimeField(
       name='entrega',
       default_method='getDataMinima',       
       widget=atapi.CalendarWidget(
           label="Data de Entrega",
           show_hm=False,
           format='%d/%m/%Y',
           starting_year='2014',           

       ),
    ),

    atapi.LinesField(
        name='responsabel',
        widget=atapi.InAndOutWidget(
            label="Responsável pela tarefa",
        ),
        vocabulary='getListaCriacao',
    ),

    atapi.TextField(
        name='observacoes',
        widget=atapi.TextAreaWidget(
            label="Observações",
        ),
    allowable_content_types="('text/html','text/plain')",
    default_output_type="text/html",
    searchable=1,
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

CriacaoSchema['title'].storage = atapi.AnnotationStorage()
CriacaoSchema['title'].widget.label = _(u"Demanda")

CriacaoSchema['description'].storage = atapi.AnnotationStorage()
CriacaoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
CriacaoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(CriacaoSchema, moveDiscussion=False)


class Criacao(base.ATCTContent):
    """''"""
    implements(ICriacao)

    meta_type = "Criacao"
    schema = CriacaoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    def getListaCriacao(self):
        """ Retorna a lista de membros presentes no grupo
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('criacao')
        members = group.getGroupMembers()
        list = DisplayList()
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.add(memberId, fullname)
        return list


atapi.registerType(Infografia, PROJECTNAME)
