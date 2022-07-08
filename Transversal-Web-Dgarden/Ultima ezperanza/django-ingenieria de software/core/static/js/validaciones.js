$(document).ready(function () {
    //Validacion Email Registro
$("#email").on("input", function() {
    if($("#email").val().indexOf('@', 0) == -1 || $("#email").val().indexOf('.', 0) == -1){
        $("#email").removeClass("ok");
            $("#mensaje").html("Ingrese un correo electronico valido !!!!.");
    }else{
    
        $("#mensaje").html("");
    }
}

    
);
    //validacion Nombre Registro 
$("#nombre").on("input",function(){
    if ($("#nombre").val() == "") {
        $("#email").removeClass("ok");
        $("#mensaje1").html("Ingrese un nombre !!!!.");

    }else{
        $("#mensaje1").html("");

    }

});

$("#contra").on("input",function(){
    
    if ($("#contra").val() == "")  {
        $("#mensaje2").html("Ingrese una contraseña valida  !!!!.");

    }else {
        $("#mensaje2").html("");

    }

});
$("#contra").on("input",function(){
    if ($("#contra").val().length < 4)  {
        $("#mensaje3").html("La contraseña debe tener al menos 4 caracteres");

    }else{
        $("#mensaje3").html("");
        
    }

});


});

$('#btnIngreso').on('click', function(e){

    e.preventDefault();

    nombreUsuario = $('#nombreUsuario');
    contrasena = $('#contrasena');


    // if(validaFormulario()){
    //     alertify.alert('Inicio de sesión exitoso', Bienvenido "${nombreUsuario.val()}");
    //     setTimeout(() => {
    //         window.location.href = '../';
    //     }, 2000);
    // }

});

