from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from ebc.pauta import pautaMessageFactory as _

class IEvento(Interface):
    """Description of the Example Type"""
    
    # -*- schema definition goes here -*-
    obs_importante = schema.TextLine(
        title=_(u"Observação importante"), 
        required=False,
        description=_(u""),
    )

    data_hora = schema.Date(
        title=_(u"Data e hora do evento"), 
        required=True,
        description=_(u"Informe a data e a hora do evento."),
    )

    ordem_servico = schema.TextLine(
        title=_(u"Ordem de Serviço"), 
        required=False,
        description=_(u"Informe o numero da ordem de serviço"),
    )

    tipo = schema.List(
        title=_(u"Tipo da OS"), 
        required=False,
        description=_(u"Selecione o tipo da ordem de serviço."),
    )

    politica = schema.List(
        title=_(u"Política publica"), 
        required=True,
        description=_(u"Selecione a política publica."),
    )

    local = schema.TextLine(
        title=_(u"Local"), 
        required=False,
        description=_(u"Informe o local do evento"),
    )

    contatos = schema.TextLine(
        title=_(u"Contatos"), 
        required=False,
        description=_(u""),
    )

    flashes = schema.TextLine(
        title=_(u"Flashes"), 
        required=False,
        description=_(u""),
    )

    rodapes = schema.Text(
        title=_(u"Rodapés"), 
        required=False,
        description=_(u""),
    )

    creditos = schema.Text(
        title=_(u"Créditos"), 
        required=False,
        description=_(u""),
    )

    visita = schema.Text(
        title=_(u"Visita técnica"), 
        required=False,
        description=_(u""),
    )

    ocorrencias = schema.Text(
        title=_(u"Ocorrências"), 
        required=False,
        description=_(u""),
    )

    observacoes = schema.Text(
        title=_(u"Observações"), 
        required=False,
        description=_(u""),
    )

