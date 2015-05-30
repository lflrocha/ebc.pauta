# -*- coding: utf-8 -*-
"""Definition of the Texto content type
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
from ebc.pauta.interfaces import ITexto
from ebc.pauta.config import PROJECTNAME

TextoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((


    atapi.LinesField(
       name='midia',
       widget=atapi.SelectionWidget(
           label="Mídia/Tipo de Matéria",
           description="Selecione a Mídia/Tipo de Matéria a que este texto é destinado.",
       ),
       vocabulary='getListaMidias',
       required=True,
    ),

    atapi.TextField(
        name='texto',
        widget=atapi.TextAreaWidget(
            label="Texto",
            rows="15",
        ),
    allowable_content_types="('text/html','text/plain')",
    default_output_type="text/html",
    searchable=1,
    ),


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

TextoSchema['title'].storage = atapi.AnnotationStorage()
TextoSchema['title'].required = "False"
TextoSchema['title'].widget.visible = {"edit": "invisible", "view": "invisible"}

TextoSchema['description'].storage = atapi.AnnotationStorage()
TextoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(TextoSchema, moveDiscussion=False)



class Texto(base.ATCTContent):
    """''"""
    implements(ITexto)

    meta_type = "Texto"
    schema = TextoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    

    def getListaMidias(self):
        """ Retorna a lista das midias selecionadas na pauta.
        """
        pauta = self.aq_parent
        return pauta.getMidiasString().split(', ')



atapi.registerType(Texto, PROJECTNAME)
