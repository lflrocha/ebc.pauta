# -*- coding: utf-8 -*-
"""Definition of the Santinho content type
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

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import ISantinho
from ebc.pauta.config import PROJECTNAME

SantinhoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        name='nome',
        widget=atapi.StringWidget(
            label="Nome",
            description="Informe o nome da pessoa",
        ),
       required=True,
    ),

    atapi.StringField(
        name='credito',
        widget=atapi.StringWidget(
            label="Crédito",
        ),
    ),

    atapi.StringField(
        name='local',
        widget=atapi.StringWidget(
            label="Local",
        ),
    ),

    atapi.ImageField(
        name='foto',
        widget=atapi.ImageWidget(
            label='Foto',
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

SantinhoSchema['title'].storage = atapi.AnnotationStorage()
SantinhoSchema['title'].required = "False"
SantinhoSchema['title'].widget.visible = {"edit": "invisible", "view": "invisible"}

SantinhoSchema['description'].storage = atapi.AnnotationStorage()
SantinhoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
SantinhoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(SantinhoSchema, moveDiscussion=False)


class Santinho(base.ATCTContent):
    """Description of the Example Type"""
    implements(ISantinho)

    meta_type = "Santinho"
    schema = SantinhoSchema

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



atapi.registerType(Santinho, PROJECTNAME)
