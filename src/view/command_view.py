def get_command_view() -> str:
    message = '''
        Sistema de calculadoras

        * Calculadora - 1
        * Sair - 0

    '''
    print(message)

    command = input('\tEscolha uma opção: ')

    return command
