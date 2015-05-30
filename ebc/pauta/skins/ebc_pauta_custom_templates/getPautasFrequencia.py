## Script (Python) "getPautasFrequencia"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas do Frequencia Brasil


pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getMidias='frequencia', \
					      sort_on='getData', sort_order='reverse')

return pautas
