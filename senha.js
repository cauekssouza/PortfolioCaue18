function gerarSenha() {
    var comprimento_senha = document.getElementById("comprimento_senha").value;
    var incluir_numeros = document.getElementById("incluir_numeros").checked;
    var incluir_minusculo = document.getElementById("incluir_minusculo").checked;
    var incluir_maiusculo = document.getElementById("incluir_maiusculo").checked;
    var incluir_especial = document.getElementById("incluir_especial").checked;

    var caracteres = "abcdefghijklmnopqrstuvwxyz";
    if (incluir_numeros) caracteres += "0123456789";
    if (incluir_minusculo) caracteres += "abcdefghijklmnopqrstuvwxyz";
    if (incluir_maiusculo) caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (incluir_especial) caracteres += "!@#$%^&*()--++";

    var senha = "";
    for (var i = 0; i < comprimento_senha; i++) {
        senha += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
    }

    document.getElementById("senha").innerHTML = "Senha Gerada: " + senha;
}