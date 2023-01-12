var btn_entrar = document.querySelector('#entrar')
var esconde_div_logo = document.querySelector('#content-wrapper')
var esconde_div_produtos = document.querySelector('#produtos')
var login_cliente = document.querySelector('#login-cliente')


if(btn_entrar != null) {

    btn_entrar.addEventListener('click', function () {
        esconde_div_logo.style.display = 'none';
        esconde_div_produtos.style.display = 'none';
        login_cliente.style.display = 'block';

      })
}