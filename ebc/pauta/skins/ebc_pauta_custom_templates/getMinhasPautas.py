## Script (Python) "getMinhasPautas"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id
##title=
##
data = DateTime()-1
pautas = []


lista_grupos = ['Apresentadores', 'Cinegrafistas', 'Coordenadores', 'Pauteiros', 'infografistas']

member = context.portal_membership.getMemberById(id)
try: 
    grupos = member.getGroups()
except:
    grupos = []

if 'Reporteres' in grupos:
    pautas = context.portal_catalog.searchResults(Type="Pauta", getReporter=id, getData={"query": data, "range": "min"})
elif 'Produtores' in grupos:
    pautas = context.portal_catalog.searchResults(Type="Pauta", getProdutor=id, getData={"query": data, "range": "min"})
elif 'Editores' in grupos:
    pautas = context.portal_catalog.searchResults(Type="Pauta", getEditor=id, getData={"query": data, "range": "min"})
elif 'infografistas' in grupos:
    pautas = context.portal_catalog.searchResults(Type=['Infografia', 'Santinho', 'Servico'], review_state=['Solicitacao','Aguardando edicao','Em edicao','Pendencia'])


return pautas

