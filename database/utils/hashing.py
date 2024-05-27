import bcrypt


class utils_code:
    def hasing_data(passwd:str):

        # Generar un salt aleatorio
        salt = bcrypt.gensalt()
        # Hashear la contraseña con el salt
        hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), salt)
        # Devolver la contraseña hasheada como una cadena de bytes
        return hashed_password