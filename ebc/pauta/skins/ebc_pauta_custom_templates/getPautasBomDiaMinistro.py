## Script (Python) "getPautasBomDiaMinistro"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas do Bom Dia Ministro


pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getMidias='bomdiaministro', \
                                              sort_on='getData', \
                                              sort_order='reverse')

return pautas
