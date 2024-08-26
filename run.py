from app import app

if __name__ == '__main__':
    app.run(debug=True)
import os

# Certifique-se de que o diretório 'layouts' existe
if not os.path.exists('layouts'):
    os.makedirs('layouts')


    