## Script (Python) "getInfografiaMes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista infografias


ret = {}

infografias = context.portal_catalog.searchResults(portal_type=['Infografia','Santinho','Servico'])


for infografia in infografias:
    mes = infografia.getData.strftime('%Y%m')

    if mes in ret.keys():
        ret[mes].append(infografia)
    else:
        ret[mes] = [infografia]

return ret
