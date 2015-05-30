## Script (Python) "getInfografia"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista infografias

ret = { 'Solicitacao': [], 'Aguardando edicao': [], 'Em edicao': [], 'Finalizado': [], 'Pendencia': [], }

path = {'query': '/redacao/pautas/', 'depth':2}


pautas = context.portal_catalog.searchResults(portal_type=['Infografia','Santinho','Servico'],path=path)


limite = DateTime() -2

for pauta in pautas:
    data = pauta.getData
    rs = pauta.review_state 
    if rs == 'Finalizado':
        if DateTime(data) >= limite:
          ret[rs].append(pauta)
    else:
      ret[rs].append(pauta)

return ret
