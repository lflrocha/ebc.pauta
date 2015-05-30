## Script (Python) "getVivoMes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de pautas em arquivo
##
ret = { }

eventos = context.portal_catalog.searchResults(portal_type='Evento', \
                                              review_state=['Agendado', 'Transmitido'])

for evento in eventos:
    mes = evento.getData_hora.strftime('%Y%m')

    if mes in ret.keys():
        ret[mes].append(evento)
    else:
        ret[mes] = [evento]


return ret

