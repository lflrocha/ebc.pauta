# -*- coding: utf-8 -*-
"""Definition of the Pauta content type
"""

from zope.interface import implements, directlyProvides

from DateTime.DateTime import *
from string import join

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.ATVocabularyManager import NamedVocabulary
from Products.Archetypes.public import DisplayList

from Products.CMFCore.utils import getToolByName

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.SelectColumn import SelectColumn
from Products.DataGridField.DataGridField import FixedRow

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import IPauta
from ebc.pauta.config import PROJECTNAME

PautaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-


       atapi.TextField(
        name='pauta',
        widget=atapi.TextAreaWidget(
            label="Pauta",
        ),
    allowable_content_types="('text/html', 'text/plain')",
    default_output_type="text/html",
    searchable=1,
    required='true',
    ),

    atapi.TextField(
        name='enfoque',
        widget=atapi.TextAreaWidget(
            label="Enfoque",
        ),
    allowable_content_types="('text/html','text/plain')",
    default_output_type="text/html",
    searchable=1,
    ),

    atapi.TextField(
        name='contexto',
        widget=atapi.TextAreaWidget(
            label="Contexto",
        ),
    allowable_content_types="('text/html','text/plain')",
    default_output_type="text/html",
    searchable=1,
    ),


    atapi.TextField(
        name='observacao',
        widget=atapi.TextAreaWidget(
            label="Observação",
        ),
    allowable_content_types="('text/html','text/plain')",
    default_output_type="text/html",
    searchable=1,
    ), 
    
    atapi.DateTimeField(
       name='data',
       widget=atapi.CalendarWidget(
           label="Data",
           show_hm=False,
           format='%d/%m/%Y',
           starting_year='2012',
           ),
        required='true',
        default_method = 'getDefaultTime',
        validators=('isValidDate',),        
    ),

    atapi.LinesField(
        name='produtor',
        widget=atapi.InAndOutWidget(
            label="Produtor",
        ),
        vocabulary='getListaProdutores',
    ),

    atapi.LinesField(
        name='editor',
        widget=atapi.InAndOutWidget(
            label="Editor",
        ),
        vocabulary='getListaEditores',
    ),

    atapi.LinesField(
        name='reporter',
        widget=atapi.InAndOutWidget(
            label="Repórter",
        ),
        vocabulary='getListaReporteres',
    ),

    atapi.LinesField(
        name='apresentador',
        widget=atapi.InAndOutWidget(
            label="Apresentador",
        ),
        vocabulary='getListaApresentadores',
    ),


    atapi.LinesField(
        name='politica',
        widget=atapi.InAndOutWidget(
            label="Política Publica",
            description="Selecione uma ou mais política publica.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""PoliticaPublica"""),
        required=True,
        searchable=True,
    ),


    atapi.LinesField(
        name='midias',
        widget=atapi.InAndOutWidget(
            label="Mídias",
            description="Selecione uma ou mais mídia.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""Midias"""),
        required=True,
        searchable=True,
    ),

    atapi.LinesField(
        name='tipos',
        widget=atapi.InAndOutWidget(
            label="Tipos",
            description="Selecione uma ou mais tipo de mídia.",
        ),
        enforceVocabulary=True,
        vocabulary=NamedVocabulary("""TipoMateria"""),
        required=True,
        searchable=True,
    ),

    atapi.LinesField(
        name='turno',
        widget=atapi.MultiSelectionWidget(
            label='Turno',
            format='checkbox',
        ),
        enforceVocabulary=True,
        vocabulary=['Manhã','Tarde','Noite'],
    ),

    atapi.BooleanField(
        name='nota',
        widget=atapi.BooleanWidget(
            label='Nota',
        ),
    ),


    atapi.BooleanField(
        name='monitorar',
        widget=atapi.BooleanWidget(
            label='Monitorar',
        ),
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

PautaSchema['title'].widget.label = _(u"Retranca")
PautaSchema['title'].storage = atapi.AnnotationStorage()
PautaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
PautaSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(
    PautaSchema,
    folderish=True,
    moveDiscussion=False
)

class Pauta(folder.ATFolder):
    """''"""
    implements(IPauta)

    meta_type = "Pauta"
    schema = PautaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getDefaultTime(self):
        return DateTime()

    def getListaProdutores(self):
        """ Retorna a lista de usuários do grupo produtores
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('Produtores')
        members = group.getGroupMembers()
        list = DisplayList()
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.add(memberId, fullname)
        return list
        
    def getListaEditores(self):
        """ Retorna a lista de usuários do grupo editores
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('Editores')
        members = group.getGroupMembers()
        list = DisplayList()
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.add(memberId, fullname)
        return list

    def getListaReporteres(self):
        """ Retorna a lista de usuários do grupo reporteres
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('Reporteres')
        members = group.getGroupMembers()
        list = DisplayList()
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.add(memberId, fullname)
        return list

    def getListaApresentadores(self):
        """ Retorna a lista de usuários do grupo reporteres
        """
        pg = getToolByName(self, 'portal_groups')
        group = pg.getGroupById('Apresentadores')
        members = group.getGroupMembers()
        list = DisplayList()
        for member in members:
            memberId = member.getMemberId()
            fullname = member.getProperty('fullname', memberId)
            list.add(memberId, fullname)
        return list

    def getProdutoresString(self):
        """ Retorna os produtores selecionados em uma string
        """
        lista = ''
        selecionados = self.getProdutor()
        listacompleta = self.getListaProdutores()
        for selecionado in selecionados:
            selecionado_string = listacompleta.getValue(selecionado)
            if selecionado_string:
                lista = lista + listacompleta.getValue(selecionado) + ', '
            else:
                lista = lista + selecionado + ', ' 
        return lista

    def getEditoresString(self):
        """ Retorna os editores selecionados em uma string
        """
        lista = ''
        selecionados = self.getEditor()
        listacompleta = self.getListaEditores()
        for selecionado in selecionados:
            selecionado_string = listacompleta.getValue(selecionado)
            if selecionado_string:
                lista = lista + listacompleta.getValue(selecionado) + ', '
            else:
                lista = lista + selecionado + ', ' 
        return lista

    def getReporteresString(self):
        """ Retorna os reporteres selecionados em uma string
        """
        lista = ''
        selecionados = self.getReporter()
        listacompleta = self.getListaReporteres()
        for selecionado in selecionados:
            selecionado_string = listacompleta.getValue(selecionado)
            if selecionado_string:
                lista = lista + listacompleta.getValue(selecionado) + ', '
            else:
                lista = lista + selecionado + ', ' 
        return lista

    def getApresentadoresString(self):
        """ Retorna os reporteres selecionados em uma string
        """
        lista = ''
        selecionados = self.getReporter()
        listacompleta = self.getListaReporteres()
        for selecionado in selecionados:
            selecionado_string = listacompleta.getValue(selecionado)
            if selecionado_string:
                lista = lista + listacompleta.getValue(selecionado) + ', '
            else:
                lista = lista + selecionado + ', ' 
        return lista

    def getPoliticasSelecionadas(self):
        politica = self.getPolitica()
        return self.getSelectedVocabularyValues(politica, 'PoliticaPublica')

    def getMidiasString(self):
        """ Retorna as Midias em uma string
        """
        midias = self.getMidias()
        return self.getSelectedVocabularyValues(midias, 'Midias')

    def getTiposString(self):
        """ Retorna os Tipos em uma string
        """
        tipos = self.getTipos()
        return self.getSelectedVocabularyValues(tipos, 'TipoMateria')

    def getMarcacoes(self):
        pc = getToolByName(self, 'portal_catalog')
        path = join(self.getPhysicalPath(), '/') 
        marcacoes = pc.searchResults(path=path,Type="Marcacao",sort_on="getData")
        return marcacoes

    def getTextos(self):
        pc = getToolByName(self, 'portal_catalog')
        path = join(self.getPhysicalPath(), '/') 
        textos = pc.searchResults(path=path,Type="Texto",sort_on="getData")
        return textos

    def getInfografias(self):
        pc = getToolByName(self, 'portal_catalog')
        path = join(self.getPhysicalPath(), '/') 
        infografias = pc.searchResults(path=path,Type=['Infografia','Santinho','Servico'],sort_on="getData")
        return infografias


    def getSelectedVocabularyValue(self, selection, vocabName):
        if selection:
            atvm = getToolByName(self, 'portal_vocabularies')
            vocab = atvm.getVocabularyByName(vocabName)
            dict = vocab.getVocabularyDict(self)
            return dict[selection]
        return None

    def getSelectedVocabularyValues(self, selections, vocabName):
        atvm = getToolByName(self, 'portal_vocabularies')
        vocab = atvm.getVocabularyByName(vocabName)
        dict = vocab.getVocabularyDict(self)
        result = ''
        for value in selections:
            result = result + dict[value] + ', '
        return result[:-2]

atapi.registerType(Pauta, PROJECTNAME)
