import PySimpleGUI as sg


class Calculator:

    def __init__(self):
        # layout
        layout = [
            [sg.Text('1th Number', size=(12, 0)), sg.Input(key='num1', size=(5, 0))],
            [sg.Text('2th Number', size=(12, 0)), sg.Input(key='num2', size=(5, 0))],
            [sg.Text('Choose the operation:')],
            [sg.Radio('+', 'operation', key='+'), sg.Radio('-', 'operation', key='-'),
             sg.Radio('x', 'operation', key='*'), sg.Radio('/', 'operation', key='/')],
            [sg.Button('Calculate')],
            [sg.Output(size=(20, 10))]
        ]
        # window
        self.janela = sg.Window("Calculator").layout(layout)

    def value(self):
        self.janela.fill(self)
        return self

    def iniciate(self):
        while True:
            self.button, self.values = self.janela.Read()
            num1 = self.values['num1']
            num2 = self.values['num2']
            if self.values['+']:
                try:
                    resultado = float(num1) + float(num2)
                    print(resultado)
                except ValueError:
                    print('Utilize apenas números!')
            elif self.values['-']:
                try:
                    resultado = float(num1) - float(num2)
                    print(resultado)
                except ValueError:
                    print('Utilize apenas números!')
            elif self.values['*']:
                try:
                    resultado = float(num1) * float(num2)
                    print(resultado)
                except ValueError:
                    print('Utilize apenas números!')
            elif self.values['/']:
                try:
                    resultado = float(num1) / float(num2)
                    print(resultado)
                except ValueError:
                    print('Utilize apenas números!')



tela = Calculator()
tela.iniciate()


