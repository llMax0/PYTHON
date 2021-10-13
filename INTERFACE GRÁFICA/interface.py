from PySimpleGUI import PySimpleGUI as sg #biblioteca de criação de interface gráfica

#layout 

sg.theme('Reddit') #temas para layout, existem muitos, só pesquisar
layout = [ #foi inserido na variável 'layout' as informações que irão constar na janela
    [sg.Text('Usuário'), sg.Input(key='usuário', size=(20,1))],# l1 - adicionar os elementos necessários (texto e input) - identificador 'key' para acessar a informação do input posteriormente.
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],#password_char '*' tem a função de dar o input sem exibir a senha na tela
    [sg.Checkbox('Salvar informações?')],#geração de uma caixa para ser marcada
    [sg.Button('ENTRAR')]#criação de botão para realização do EVENTO - dispara o evento do ato de clicar no botão de nome 'entrar'
] #(a janela é formada de acordo com os eixos X e Y, logo, por linhas e colunas - no caso, 3 linhas)

#janela 

janela = sg.Window('Tela de Login', layout)#na variavel 'janela' foi inserido o comando para ariação da janela de fato - recebe diversosparâmetros - o padrão foi: título da janela e o leyout de fato que vou construído na variável de mesmo nome

#eventos
while True: #o programa não para de rodar
    eventos, valores = janela.read() #as informações são lidas e inseridas nas varáveis 'eventos' e 'valores'
    if eventos == sg.WINDOW_CLOSED:
        break
   