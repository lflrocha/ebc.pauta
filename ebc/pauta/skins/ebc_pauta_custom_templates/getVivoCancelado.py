## Script (Python) "getVivoCancelado"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de eventos do vivo - Cancelados
##
eventos = context.portal_catalog.searchResults(portal_type='Evento',    \
                                               review_state='Cancelado', \
                                               sort_on='getData_hora')

return eventos
