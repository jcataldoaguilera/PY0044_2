$(document).ready(function (){
    /* Tooltip correo y favoritos */
    $('[data-toggle="tooltip"]').tooltip();
    /* Alerta al clickear */
    $('#enviarCorreo').on("click", function (){
        alert("El correo fue enviado correctamente...")
    });
    /* Color rojo a INGREDIENTES y PREPARACION al hacer dblclick */
    $('h4').on("dblclick", function (){
        $(this).css("color", "red")
    });
    /* Ocultar card-text al hacer click sobre el titulo de las tarjetas */
    $('.card-title').on("click", function (){
        $('.card-text').toggle()
    });
});