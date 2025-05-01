// Funções para abrir e fechar o menu

const button_menu = document.querySelector('#button_menu');
const menu_options = document.querySelector('.container_options');
const button_fechar = document.querySelector('#button_fechar');

button_menu.addEventListener('click', function()
{
    // acessando diretamente o css pelo html da tag
    menu_options.style.display = 'flex';
});

button_fechar.addEventListener('click', function()
{
    // Troca o 'display: flex;' por 'display: none;' no css do html
    menu_options.style.display = 'none';
});




const flex = document.querySelector('#button_flex');
const block = document.querySelector('#button_block');

const body = document.querySelector('body');
const header = document.querySelector('header');
const img_menu = document.querySelector('img[alt = "menu"]');
const main = document.querySelector('main');
const h1 = document.querySelector('h1');
const h3 = document.querySelector('h3');
const img_logout = document.querySelector('img[alt = "logout"]');
const container = document.querySelector('.container');
const container_comentario = document.querySelector('.container_comentario');
const comentarios = document.querySelector('.comentarios');
const label = document.querySelector('label');
const button_enviar = document.querySelector('#button_enviar');
const input_mensagem = document.querySelector('.input_mensagem');
const container_chat = document.querySelector('.container_chat');
const texto_aviso = document.querySelector('#texto_aviso');

const verificaMedia = () =>
{
    // A função 'window.matchMedia()' recebe uma string de consulta de mídia(do css) e retorna um objeto 'MediaQueryList'. Esse objeto tem uma propriedade 'matches' que indica se a consulta de mídia é verdadeira no momento.
    if(window.matchMedia('(max-width: 760px)').matches)
    {
        console.log('Media (max-width: 760px) está ativa.');

        // No celular não é nescessário ter uma aba para mudar o layout do site
        header.style.display = 'none';
    }

    else if(window.matchMedia('(min-width: 760px) and (max-width: 1380px)').matches)
    {
        console.log('Media query (min-width: 760px) e (max-width: 1380px) está ativa.');

        // Se uma pessoa for aumentar o zoom da tela o suficiente para entrar no 'display: none;' do celular, quando ele voltar para a o tamanho da tela normal do dispositivo, o 'display' se tornará 'flex' novamente.
        header.style.display = 'flex';

        // chamando variavel criada acima desta função 
        flex.addEventListener('click', function()
        {
            main.style.height = 'auto';

            container.style.flexDirection = 'column';

            container_comentario.style.width = '70%';
            container_comentario.style.height = '300px';
            container_comentario.style.margin = '20px auto';

            comentarios.style.height = '100%';

            input_mensagem.style.maxWidth = '80%';

            container_chat.style,height = '400px'
            container_chat.style.margin = '20px auto';
        });

        // chamando variavel criada acima desta função 
        block.addEventListener('click', function()
        {
            main.style.height = 'auto';

            container.style.flexDirection = 'row';

            container_comentario.style.width = '20%';
            container_comentario.style.height = '300px';

            comentarios.style.height = '100%';

            input_mensagem.style.maxWidth = '100%';

            container_chat.style.width = '70%';
            container_chat.style.height = '300px';
            container_chat.style.margin = '20px';
        });
    }

    else if(window.matchMedia('(min-width: 1380px)').matches)
    {
        console.log('Media query (min-width: 1380px) está ativa.');

        header.style.display = 'flex';

        flex.addEventListener('click', function()
        {
            main.style.height = '1150px';

            container.style.flexDirection = 'column';

            container_comentario.style.width = '70%';
            container_comentario.style.height = '400px';
            container_comentario.style.margin = '20px auto';

            input_mensagem.style.maxWidth = '80%';
            
            container_chat.style.width = '80%';
            container_chat.style.height = '400px';
            container_chat.style.margin = '20px auto';
        });


        block.addEventListener('click', function()
        {
            main.style.height = '800px';

            container.style.flexDirection = 'row';

            container_comentario.style.width = '20%';
            container_comentario.style.height = '500px';
            container_comentario.style.margin = '20px';

            input_mensagem.style.maxWidth = '100%';

            container_chat.style.width = '70%';
            container_chat.style.height = '500px';
            container_chat.style.margin = '20px';
        });
    }

    else
    {
        //Não sei como será usado, mas é melhor prevenir do que remediar. 
        console.log('Nenhuma das media queries especificadas está ativa.');
    }
}
  
// Chama a função para verificar no carregamento da página.
verificaMedia();

// Adiciona listeners(ouvinte esperamdo pelo evento) no para verificar quando a tela for redimensionada.
window.addEventListener('resize', verificaMedia);


const button_white = document.querySelector('#button_white');
const button_black = document.querySelector('#button_black');

button_white.addEventListener('click', function()
    {
        flex.style.color = 'var(--preto)';
        block.style.color = 'var(--preto)';
        button_white.style.color = 'var(--preto)';
        button_black.style.color = 'var(--preto)';
        button_fechar.style.color = 'var(--preto)';

        button_menu.style.background = 'var(--branco)';
        flex.style.background = 'var(--branco)';
        block.style.background = 'var(--branco)';
        button_white.style.background = 'var(--branco)';
        button_black.style.background = 'var(--branco)';
        button_fechar.style.background = 'var(--branco)';

        button_menu.style.border = '2px solid var(--preto)';
        flex.style.border = ' 2px solid var(--preto)';
        block.style.border= ' 2px solid var(--preto)';
        button_white.style.border = ' 2px solid var(--preto)';
        button_black.style.border = ' 2px solid var(--preto)';
        button_fechar.style.border = ' 2px solid var(--preto)';


        h1.style.color = 'var(--preto)';
        h3.style.color = 'var(--preto)';
        button_enviar.style.color = 'var(--preto)';
        label.style.color = 'var(--preto)';
        texto_aviso.style.color = 'var(--preto)';


        body.style.background = 'var(--branco)';
        main.style.background = 'var(--branco)';

        main.style.border = '4px solid var(--preto)';
        container_comentario.style.border = '4px solid var(--preto)'
        container_chat.style.border = '4px solid var(--preto)'

        img_menu.src = '../static/icons/menu_white.svg';
        img_logout.src = '../static/icons/logout_black.png';


    });

button_black.addEventListener('click', function()
    {
        flex.style.color = 'var(--dourado)';
        block.style.color = 'var(--dourado)';
        button_white.style.color = 'var(--dourado)';
        button_black.style.color = 'var(--dourado)';
        button_fechar.style.color = 'var(--dourado)';

        button_menu.style.background = 'var(--preto)';
        flex.style.background = 'var(--preto)';
        block.style.background = 'var(--preto)';
        button_white.style.background = 'var(--preto)';
        button_black.style.background = 'var(--preto)';
        button_fechar.style.background = 'var(--preto)';

        button_menu.style.border = '2px solid var(--branco)';
        flex.style.border = ' 2px solid var(--branco)';
        block.style.border= ' 2px solid var(--branco)';
        button_white.style.border = ' 2px solid var(--branco)';
        button_black.style.border = ' 2px solid var(--branco)';
        button_fechar.style.border = ' 2px solid var(--branco)';


        h1.style.color = 'var(--dourado)';
        h3.style.color = 'var(--dourado)';
        button_enviar.style.color = 'var(--dourado)';
        label.style.color = 'var(--dourado)';
        texto_aviso.style.color = 'var(--dourado)';

        body.style.background = 'var(--preto)';
        main.style.background = 'var(--azul_escuro)';

        main.style.border = '4px solid var(--dourado)';
        container_comentario.style.border = '4px solid var(--marrom)';
        container_chat.style.border = '4px solid var(--marrom)';

        img_menu.src = '../static/icons/menu_black.svg';
        img_logout.src = '../static/icons/logout_white.png';
    });
