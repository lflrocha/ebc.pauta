## Script (Python) "getPautasNbrEntrevista"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas do Documentacao


pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getMidias='documentacao', \
                                              sort_on='getData', sort_order='reverse')

return pautas
