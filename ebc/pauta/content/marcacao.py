# -*- coding: utf-8 -*-
"""Definition of the Marcacao content type
"""

from zope.interface import implements, directlyProvides

from DateTime import DateTime

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.Archetypes.public import DisplayList
from Products.CMFCore.utils import getToolByName

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import IMarcacao
from ebc.pauta.config import PROJECTNAME

MarcacaoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((


    atapi.StringField(
        name='entrevistado',
        widget=atapi.StringWidget(
            label='Entrevistado',
        ),
    ),

    atapi.DateTimeField(
       name='data',
       default_method=DateTime,       
       widget=atapi.CalendarWidget(
           label="Data e Hora",
       ),
    ),

    atapi.LinesField(
        name='reporter',
        widget=atapi.InAndOutWidget(
            label="Repórter",
        ),
        vocabulary='getListaReporteres',
    ),

    atapi.LinesField(
        name='cinegrafista',
        widget=atapi.InAndOutWidget(
            label="Cinegrafista/Auxiliar",
        ),
        vocabulary='getListaCinegrafistas',
    ),

    atapi.StringField(
        name='fita',
        widget=atapi.StringWidget(
            label='Fita',
            size='10',
            maxlength='10',
        ),
    ),

    atapi.TextField(
        name='contato',
        widget=atapi.TextAreaWidget(
            label='Contato',
        ),
        allowable_content_types="('text/html', 'text/plain')",
        default_output_type="text/html",
    ),

    atapi.TextField(
        name='local',
        widget=atapi.TextAreaWidget(
            label='Local',
        ),
        allowable_content_types="('text/html', 'text/plain')",
        default_output_type="text/html",
    ),

    atapi.TextField(
        name='observacoes',
        widget=atapi.TextAreaWidget(
            label='Observações',
        ),
        allowable_content_types="('text/html', 'text/plain')",
        default_output_type="text/html",
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

MarcacaoSchema['title'].storage = atapi.AnnotationStorage()
MarcacaoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
MarcacaoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(MarcacaoSchema, moveDiscussion=False)

class Marcacao(base.ATCTContent):
    """''"""
    implements(IMarcacao)

    meta_type = "Marcação"
    schema = MarcacaoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getListaReporteres(self):
        """ Retorna a lista de membros presentes no grupo
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('Reporteres')
        members = group.getGroupMembers()
        list = []
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.append((memberId, fullname)) 
        return DisplayList(list)

    def getListaCinegrafistas(self):
        """ Retorna a lista de membros presentes no grupo
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('Cinegrafistas')
        members = group.getGroupMembers()
        list = []
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.append((memberId, fullname)) 
        return DisplayList(list)


    def getReporteresString(self):
        """ Retorna os reporteres selecionados em uma string
        """
        string = ''
        selecionados = self.getReporter()
        listacompleta = self.getListaReporteres()
        for selecionado in selecionados:
            string = string + listacompleta.getValue(selecionado) + ', '
        return string
    

    def getCinegrafistasString(self):
        """ Retorna os reporteres selecionados em uma string
        """
        string = ''
        selecionados = self.getCinegrafista()
        listacompleta = self.getListaCinegrafistas()
        for selecionado in selecionados:
            string = string + listacompleta.getValue(selecionado) + ', '
        return string


atapi.registerType(Marcacao, PROJECTNAME)
