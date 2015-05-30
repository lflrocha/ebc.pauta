## Script (Python) "getPautasSugestoesTodas"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna todas as sugestoes de pautas


ret = { }

pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              sort_on='getData', \
                                              review_state='Sugestao')

for pauta in pautas:
    mes = pauta.getData.strftime('%Y%m')

    if mes in ret.keys():
        ret[mes].append(pauta)
    else:
        ret[mes] = [pauta]

return ret
