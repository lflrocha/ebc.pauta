## Script (Python) "getPautasCafe"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas do Cafe


pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getMidias='cafe', \
					                          sort_on='getData', \
					                          sort_order='reverse')

return pautas
