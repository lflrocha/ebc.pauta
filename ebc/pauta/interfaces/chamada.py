from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from ebc.pauta import pautaMessageFactory as _

class IChamada(Interface):
    """Description of the Example Type"""

    episodio = schema.TextLine(
        title=_(u"Episódio"), 
        required=False,
        description=_(u"Field description"),
    )

    fita_programa = schema.TextLine(
        title=_(u"Fita do programa"), 
        required=False,
        description=_(u"Field description"),
    )

    exibicao_programa = schema.Date(
        title=_(u"Data de exibição do programa"), 
        required=False,
        description=_(u"Field description"),
    )

#    recebedor = schema.TextLine(
#        title=_(u"Recebedor"), 
#        required=False,
#        description=_(u"Field description"),
#    )

