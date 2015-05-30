## Script (Python) "getPautasSugestoesTodas"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data=''
##title=Retorna a lista de pautas em producao

ret = { 'manha': [], 'tarde': [], 'noite': [], 'nbrentrevista': [], 'notas': [] }

if not data:
    data = DateTime().Date()

pautas = context.portal_catalog.searchResults(portal_type='Vivo', \
                                              getData=data, \
										      review_state='Pautao')

for pauta in pautas:
    obj = pauta.getObject()
    turno = obj.getTurno()
    midias = obj.getMidias()

    for midia in midias:
        if 'nbr-entrevista' in midia['midia']:
            ret['nbrentrevista'].append(pauta)

        if 'nota' in midia['midia']:
            ret['notas'].append(pauta)

    if 'Manh\xc3\xa3' in turno:
        ret['manha'].append(pauta)
    if 'Tarde' in turno:
        ret['tarde'].append(pauta)
    if 'Noite' in turno:
        ret['noite'].append(pauta)

    

return ret
