## Script (Python) "getVivoSemana"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data=''
##title=Retorna a lista de eventos do vivo
##
ret = { }


min = DateTime('2013-01-01 00:00:00')


dr =  {'query':(min), 'range': 'min'}


eventos = context.portal_catalog.searchResults(portal_type='Evento', \
                                              review_state=['Agendado', 'Transmitido'],\
                                              getData_hora=dr)

for evento in eventos:
    semana = evento.getData_hora.strftime('%U')

    if semana in ret.keys():
        ret[semana].append(evento)
    else:
        ret[semana] = [evento]


return ret
