# -*- coding: utf-8 -*-
"""Definition of the Infografia content type
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

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from collective.datagridcolumns.TextAreaColumn  import TextAreaColumn

from Products.validation.validators.ExpressionValidator import ExpressionValidator

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import IInfografia
from ebc.pauta.config import PROJECTNAME

InfografiaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((


    DataGridField(
        name='telas',
        columns=("titulo", "texto", "texto_off"),        
        widget=DataGridWidget(
            label='Tela',
            columns={
                'titulo' : Column("Título"),
                'texto' : TextAreaColumn("Texto Letreiro/Fonte"),
                'texto_off' : TextAreaColumn("Texto do Off"),
            }            
        ),
        required=True,
    ),

    atapi.FileField(
        name='arquivo',
        widget=atapi.FileWidget(
            label='Arquivo do Off',
        ),
    ),

    atapi.DateTimeField(
       name='entrega',
       default_method='getDataMinima',       
       widget=atapi.CalendarWidget(
           label="Entrega",
           description="Data e hora limite para entrega",
       ),
       required=True,
       validators=('isValidDate', ExpressionValidator('python: DateTime(value) > DateTime()+0.084', 'A hora de entega deve ser, no mínimo, duas horas maior que a hora atual.'), ),

    ),

    atapi.LinesField(
        name='infografista',
        widget=atapi.InAndOutWidget(
            label="Videografista",
            description="Campo de preenchimento exclusivo pela Gerência de Criação"
        ),
        vocabulary='getListaInfografistas',
        schemata="Arte",
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

InfografiaSchema['title'].storage = atapi.AnnotationStorage()
InfografiaSchema['title'].required = "False"
InfografiaSchema['title'].widget.visible = {"edit": "invisible", "view": "invisible"}

InfografiaSchema['description'].storage = atapi.AnnotationStorage()
InfografiaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
InfografiaSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(InfografiaSchema, moveDiscussion=False)


class Infografia(base.ATCTContent):
    """''"""
    implements(IInfografia)

    meta_type = "Infografia"
    schema = InfografiaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    def Title(self):
	return self.aq_parent.Title()

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


atapi.registerType(Infografia, PROJECTNAME)
