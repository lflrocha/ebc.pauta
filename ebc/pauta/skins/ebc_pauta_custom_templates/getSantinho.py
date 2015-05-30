## Script (Python) "getInfografia"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista infografias

ret = { 'Solicitacao': [], 'Aguardando edicao': [], 'Em edicao': [], 'Finalizado': [], 'Pendencia': [], }

pautas = context.portal_catalog.searchResults(portal_type='Santinho')


for pauta in pautas:
    obj = pauta.getObject()
    rs = pauta.review_state 
    ret[rs].append(pauta)

return ret