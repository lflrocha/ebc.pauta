# -*- coding: utf-8 -*-
"""Definition of the especial content type
"""

from zope.interface import implements, directlyProvides

from DateTime import DateTime

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.Archetypes.public import DisplayList
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.CMFCore.utils import getToolByName

from ebc.pauta import pautaMessageFactory as _
from ebc.pauta.interfaces import IEspecial
from ebc.pauta.config import PROJECTNAME

EspecialSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.DateTimeField(
       name='data',
       default_method=DateTime,       
       widget=atapi.CalendarWidget(
           label="Data do especial",
           show_hm=False,
           format='%d/%m/%Y',
           starting_year='2011',           
       ),
    ),

    atapi.ReferenceField(
        name='pautas',
        relationship='FazParte',
        widget=ReferenceBrowserWidget(
            label='Pautas',
            base_query={'portal_type': 'Pauta', 'sort_on': 'created', 'sort_order': 'reverse'},
            allow_browse=0,
            allow_search=1,
            show_results_without_query=1,
        ),
        multiValued=True,
    ),    

    atapi.StringField(
        name='contato',
        widget=atapi.TextAreaWidget(
            label='Contato',
        ),
    ),

    atapi.StringField(
        name='local',
        widget=atapi.TextAreaWidget(
            label='Local',
        ),
    ),

    atapi.StringField(
        name='observacoes',
        widget=atapi.TextAreaWidget(
            label='Observações',
        ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

EspecialSchema['title'].storage = atapi.AnnotationStorage()
EspecialSchema['title'].widget.label = _(u"Especial")
EspecialSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
EspecialSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(EspecialSchema, moveDiscussion=False)

class Especial(base.ATCTContent):
    """''"""
    implements(IEspecial)

    meta_type = "Especial"
    schema = EspecialSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-


atapi.registerType(Especial, PROJECTNAME)
