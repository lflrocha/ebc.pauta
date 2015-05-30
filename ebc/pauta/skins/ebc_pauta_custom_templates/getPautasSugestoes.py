## Script (Python) "getPautasEmProducao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data=''
##title=Retorna a lista de pautas em producao


ret = { }

if not data:
    data = DateTime().Date()

pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getData=data, \
                                              sort_on='sortable_title', \
                                              review_state='Sugestao')

return pautas
