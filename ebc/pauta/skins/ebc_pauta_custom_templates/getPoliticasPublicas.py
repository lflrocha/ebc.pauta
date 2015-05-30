## Script (Python) "getInfografia"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna a lista infografias

pautas = context.portal_vocabularies.getVocabularyByName('PoliticaPublica')


return pautas.getVocabularyDict()


