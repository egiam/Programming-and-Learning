$(document).ready(handler: function(){

    var span = $('span');
    span.css(propertyName: 'border', value_function:'1px solid blue')
    console.log(span.text());

    var atributo = $('[title="google"]');
    atributo.css(propertyName: 'font-size', value_function:'50px');
    console.log(atributo.text());

})