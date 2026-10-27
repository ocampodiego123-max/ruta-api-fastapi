from getpass import getpass
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

contrasena = getpass("Introduce la contraseña que usarás para iniciar sesión: ")

hash_generado = password_hash.hash(contrasena)

print("\nHash generado:")
print(hash_generado)