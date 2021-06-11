from cryptography.fernet import Fernet
class Codificador:
    def __init__(self, archivo_clave=None):
        self.__clave = None
        if archivo_clave:
            self.__clave = self.carga_clave(archivo_clave)

    # Método que genera la clave
    @classmethod
    def genera_clave(cls, archivo):
        clave = Fernet.generate_key()
        with open (archivo, "wb") as archivo_clave:
            archivo_clave.write(clave)
        return  "Tu clave ha sido generada en el archivo indicado"

    # Método para cargar clave
    @classmethod
    def carga_clave(cls, archivo):
        return open(archivo, "rb").read()

    #método de encriptado
    def encript(self, nom_archivo):
        f = Fernet(self.__clave)
        with open(nom_archivo, "rb") as file:
            archivo_info = file.read()
        encrypted_data = f.encrypt(archivo_info)
        with open(nom_archivo + ".crypt", "wb") as file:
            file.write(encrypted_data)
        return "Tu archivo ha sido encriptado"

    # Método de desencriptado
    def desencript(self, nom_archivo_entrada, nom_archivo_salida):
        f = Fernet(self.__clave)
        with open(nom_archivo_entrada, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(nom_archivo_salida, "wb") as file:
            file.write(decrypted_data)
