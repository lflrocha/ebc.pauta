## Script (Python) "getPautasPautao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data='',
##title=Retorna a lista de pautas do pautao

ret = { 'manha': [], 'tarde': [], 'noite': [], 'nota':[], 'programas': [], 'semturno': [] }

if not data:
    data = DateTime().Date()

pautas = context.portal_catalog.searchResults(portal_type='Pauta', \
                                              getData=data, \
                                              review_state='Pautao')

programas = ['nbr-entrevista', 'documentacao', 'bomdiaministro', 'cenasdobrasil', 'brasilempauta', 'cafe' ]

for pauta in pautas:
    turno = pauta.getTurno
    midias = pauta.getMidias
    nota = pauta.getNota

    if nota:
        ret['nota'].append(pauta)      
    else:
        if [x for x in midias for y in programas if x == y]:
            ret['programas'].append(pauta)
        else:
            if not turno:
                ret['semturno'].append(pauta)
            else:
                if 'Manh\xc3\xa3' in turno:
                    ret['manha'].append(pauta)
                if 'Tarde' in turno:
                    ret['tarde'].append(pauta)
                if 'Noite' in turno:
                    ret['noite'].append(pauta)


return ret
