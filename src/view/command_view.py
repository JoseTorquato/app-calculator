def get_command_view() -> str:
    message = '''
        Sistema de calculadoras

        * Calculadora Averege - 1
        * Calculadora STD - 2
        * Calculadora Var - 3
        * Sair - 0

    '''
    print(message)

    command = input('\tEscolha uma opção: ')

    return command
