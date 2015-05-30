## Script (Python) "getPautasEmProducao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas em producao


ret = { }

data = DateTime().Date()

pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getData={"query": data, "range": "min"}, \
                                              getMidias=['a-voz-do-brasil','nbr-noticias'], \
                                              review_state='Em producao')

for pauta in pautas:
    mes = pauta.getData.strftime('%Y%m')

    if mes in ret.keys():
        ret[mes].append(pauta)
    else:
        ret[mes] = [pauta]

return ret
