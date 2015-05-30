## Script (Python) "getMarcacoesTodas"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data='',
##title=Retorna a lista de pautas do pautao

if not data:
    data = DateTime().Date()

dataMin =  DateTime(data).strftime("%Y/%m/%d 00:00:00")
dataMax =  DateTime(data).strftime("%Y/%m/%d 23:59:59")

pautas = context.portal_catalog.searchResults(portal_type='Marcacao', \
											  getData={"query": (DateTime(dataMin),DateTime(dataMax)), "range": "min:max"}, \
											  sort_on='getData' )

return pautas
