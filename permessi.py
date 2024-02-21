import os

# Ottieni il percorso della directory corrente
directory_path = os.path.dirname(os.path.abspath(__file__))

try:
    # Imposta i permessi della directory per la scrittura
    os.chmod(directory_path, 0o755)
    print("Permessi di scrittura impostati con successo.")
except OSError:
    print("Errore nell'impostazione dei permessi di scrittura.")
