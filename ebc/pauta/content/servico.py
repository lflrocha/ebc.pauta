# -*- coding: utf-8 -*-
"""Definition of the Servico content type
"""

from zope.interface import implements, directlyProvides
import datetime
from DateTime import DateTime

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.utils import dt2DT

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from collective.datagridcolumns.TextAreaColumn import TextAreaColumn

from Products.Archetypes.public import DisplayList
from Products.CMFCore.utils import getToolByName

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import IServico
from ebc.pauta.config import PROJECTNAME

ServicoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    DataGridField(
        name='servicos',
        columns=("texto", "texto_off"),        
        widget=DataGridWidget(
            label="Serviço",
            columns={
                'texto' : TextAreaColumn("Texto/Letreiro"),
                'texto_off' : TextAreaColumn("Texto do Off"),
            }            
        ),
        required=True,
    ),

    atapi.DateTimeField(
       name='entrega',
       default_method='getDataMinima',       
       widget=atapi.CalendarWidget(
           label="Entrega",
           description="Data e hora limite para entrega",
       ),
       required=True,
       validators=('isValidDate',),
    ),

    atapi.LinesField(
        name='infografista',
        widget=atapi.InAndOutWidget(
            label="Infografista",
            description="Campo de preenchimento exclusivo pela Gerência de Criação"
        ),
        vocabulary='getListaInfografistas',
        schemata="Arte",
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

ServicoSchema['title'].storage = atapi.AnnotationStorage()
ServicoSchema['title'].required = "False"
ServicoSchema['title'].widget.visible = {"edit": "invisible", "view": "invisible"}


ServicoSchema['description'].storage = atapi.AnnotationStorage()
ServicoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
ServicoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(ServicoSchema, moveDiscussion=False)

class Servico(base.ATCTContent):
    """Description of the Example Type"""
    implements(IServico)

    meta_type = "Servico"
    schema = ServicoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    def getDataMinima(self):
        """ 
        """
        now = datetime.datetime.now()
        delta = datetime.timedelta(hours=2)
        DT = dt2DT(now+delta)
        return DT

    def getListaInfografistas(self):
        """ Retorna a lista de membros presentes no grupo
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('infografistas')
        members = group.getGroupMembers()
        list = DisplayList()
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.add(memberId, fullname)
        return list



atapi.registerType(Servico, PROJECTNAME)
