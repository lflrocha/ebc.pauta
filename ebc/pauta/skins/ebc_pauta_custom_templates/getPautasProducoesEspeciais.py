## Script (Python) "getPautasPontoGov"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas do Ponto Gov


pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getMidias='producoes-especiais', \
                                              sort_on='getData', sort_order='reverse')

return pautas
