## Script (Python) "getChamadas"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista de chamadas

ret = { 'nova': [], 'fita_disponivel': [], 'aguardando_roteiro': [], 'produzindo_roteiro': [], 'aguardando_edicao': [], 'editando': [], 'aguardando_conferencia': [], 'entregue': [], 'aguardando_catalogacao': [], 'catalogado': [], 'enviado_matrizacao': [], 'pendencia': [], }

chamadas = context.portal_catalog.searchResults(portal_type='Chamada', sort_on='getExibicao_programa', sort_order='reverse')

limite = DateTime() -2

for pauta in chamadas:
    data = pauta.getExibicao_programa
    rs = pauta.review_state 
    if rs == 'enviado_matrizacao':
        if DateTime(data) >= limite:
            ret[rs].append(pauta)
    else:
        ret[rs].append(pauta)


return ret
