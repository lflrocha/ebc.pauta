# -*- coding: utf-8 -*-
from Products.validation.interfaces.IValidator import IValidator

class DuracaoValidator:
    __implements__ = IValidator

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kwargs):

        veiculacoes = value
        for veiculacao in veiculacoes:
            entrada = veiculacao['entrada']
            saida = veiculacao['saida']
            duracao = veiculacao['duracao']
            index = veiculacao['orderindex_']

            if index <> 'template_row_marker': 

                # Hora de entrada
                aux_entrada = entrada.split(':')

                entrada_h = 0
                entrada_m = 0

                if len(aux_entrada) <> 2:
                    return("'%s' não está no formato hh:mm (Err 01)" % str(entrada))
                else:
                    entrada_h = aux_entrada[0]
                    entrada_m = aux_entrada[1]

                try:
                    entrada_h = int(entrada_h)
                    entrada_m = int(entrada_m)
                except:
                    return("'%s' não está no formato hh:mm (Err 02)" % str(entrada))

                if len(aux_entrada[1]) <> 2:
                    return("'%s' tem valores inválidos (Err 03)" % str(entrada))                
                    
                if (entrada_h < 0 or entrada_h > 23) or (entrada_m < 0 or entrada_m > 59):
                    return("'%s' tem valores inválidos (Err 04)" % str(entrada))                

                # Hora de saída
                aux_saida = saida.split(':')

                saida_h = 0
                saida_m = 0

                if len(aux_saida) <> 2:
                    return("'%s' não está no formato hh:mm (Err 01)" % str(saida))
                else:
                    saida_h = aux_saida[0]
                    saida_m = aux_saida[1]

                try:
                    saida_h = int(saida_h)
                    saida_m = int(saida_m)
                except:
                    return("'%s' não está no formato hh:mm (Err 02)" % str(saida))

                if len(aux_saida[1]) <> 2:
                    return("'%s' tem valores inválidos (Err 03)" % str(saida))                
                    
                if (saida_h < 0 or saida_h > 23) or (saida_m < 0 or saida_m > 59):
                    return("'%s' tem valores inválidos (Err 04)" % str(saida))                


        # If we get this far something really bad happened
        # perhaps integer overflow or something else reallt annoying
        return 1
