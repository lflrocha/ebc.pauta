## Script (Python) "getPautasArquivo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas em arquivo


ret = { }

pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              review_state='Arquivo')

for pauta in pautas:
    mes = pauta.getData.strftime('%Y%m')

    if mes in ret.keys():
        ret[mes].append(pauta)
    else:
        ret[mes] = [pauta]


return ret
