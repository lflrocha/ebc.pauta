## Script (Python) "getPautasNbrEntrevista"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas do NBR Entrevista


pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getMidias='nbr-entrevista', \
                                              review_state='Em producao', \
                                              sort_on='getData', sort_order='reverse')

return pautas
