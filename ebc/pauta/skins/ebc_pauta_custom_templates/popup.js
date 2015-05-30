jq(document).ready(function(){
  jq('#ssolicitacoes a').prepOverlay({
    subtype: 'ajax',
    filter: '#content>*',
    formselector: 'form',
    });
});