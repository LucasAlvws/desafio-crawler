$(function(){
    $("#txtBusca").keyup(function(){
        var texto = $(this).val().toUpperCase();

        $("#ulItens li").css("display", "block");
        $("#ulItens li").each(function(){
            if($(this).text().toUpperCase().indexOf(texto) < 0)
                $(this).css("display", "none");
        });
    });
});
