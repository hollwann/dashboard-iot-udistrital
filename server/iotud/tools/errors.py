
def get_error_msg(code: str):
    if code == 'UD001':
        return 'Petición erronea'
    elif code == 'UD002':
        return 'El correo electronico ya se encuentra registrado.'
    elif code == 'UD003':
        return 'El correo electronico NO esta registrado.'
    elif code == 'UD004':
        return 'La contraseña es incorrecta.'
    elif code == 'UD005':
        return 'Error interno de base de datos.'
    return 'Codigo de error no definido'