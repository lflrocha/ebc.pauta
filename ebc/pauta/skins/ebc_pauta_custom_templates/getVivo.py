## Script (Python) "getVivo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data=''
##title=Retorna a lista de eventos do vivo
##
ret = { 'manha': [], 'tarde': [], 'noite': [] }

if not data:
    data = DateTime().Date()


min = DateTime(data + ' 00:00:00.1')
max = DateTime(data + ' 23:59:59')


dr =  {'query':(min, max), 'range': 'min:max'}

eventos = context.portal_catalog.searchResults(portal_type='Evento', \
                                               getData_hora=dr, \
                                               sort_on='getData_hora', \
                                               review_state='Agendado')


for evento in eventos:
    hora = int(evento.getData_hora.strftime('%H'))

    if hora < 12:
        ret['manha'].append(evento)
    elif hora < 18:
        ret['tarde'].append(evento)
    else:
        ret['noite'].append(evento)

return ret