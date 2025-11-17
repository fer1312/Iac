# Importamos las librerías necesarias para cifrar y generar claves
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

def generar_clave_y_iv():
    """Genera una clave AES de 32 bytes (AES-256) y un IV de 16 bytes."""
    key = urandom(32)  # 32 bytes para AES-256
    iv = urandom(16)   # 16 bytes para el IV
    return key, iv

def encriptar(texto_plano, key, iv):
    """
    Esta función recibe un texto normal y lo encripta con AES-256 en modo CBC.
    """
    # Creamos el objeto de cifrado
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    texto_plano_bytes = texto_plano.encode('utf-8') # Convertimos el texto a bytes
    padding_length = 16 - (len(texto_plano_bytes) % 16) # Calculamos el padding (relleno) para que el texto sea múltiplo de 16 bytes
    padding = bytes([padding_length]) * padding_length
    texto_a_cifrar = texto_plano_bytes + padding # Unimos el texto con el padding

    # Encriptamos el texto
    texto_cifrado = encryptor.update(texto_a_cifrar) + encryptor.finalize()
    return texto_cifrado

def desencriptar(texto_cifrado, key, iv):
    """
    Esta función recibe un texto encriptado y lo regresa a su forma original.
    """
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())# Creamos el objeto para desencriptar
    decryptor = cipher.decryptor()
    texto_desencriptado_con_padding = decryptor.update(texto_cifrado) + decryptor.finalize() # Obtenemos el texto desencriptado (todavía con padding)
    
    # Eliminar el padding
    padding_length = texto_desencriptado_con_padding[-1]
    texto_desencriptado = texto_desencriptado_con_padding[:-padding_length]
    # Convertimos los bytes a texto normal
    return texto_desencriptado.decode('utf-8')

# --- Uso ---
# 1. Generar clave y IV (normalmente, se guardan para uso posterior)
key, iv = generar_clave_y_iv()

# 2. Texto original
texto_original = "Fernanda Dorantes Díaz"

# 3. Encriptar el mensaje
texto_encriptado = encriptar(texto_original, key, iv)
print(f"Texto encriptado: {texto_encriptado}")

# 4. Desencriptar el mensaje
texto_desencriptado = desencriptar(texto_encriptado, key, iv)
print(f"Texto desencriptado: {texto_desencriptado}")