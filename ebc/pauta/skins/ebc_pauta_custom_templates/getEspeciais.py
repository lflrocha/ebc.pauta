## Script (Python) "getEspeciais"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista especiais

especiais = context.portal_catalog.searchResults(portal_type='Especial', sort_on='getData', sort_order='reverse')

return especiais
