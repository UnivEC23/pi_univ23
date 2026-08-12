# import time
# from init import app, db
# import sys
# from multiprocessing import Process


# if __name__ == "__main__":
#     # checar por comandos dps
#     # if (len(sys.argv) > 1):
#     #     if (sys.argv[1] == "dev"):
#     #         pass
#     server = Process(target=app.run, args=('localhost', 5000, False))
#     server.start()
#     # app.run(debug=True, host='127.0.0.1', port=5000)
#     with app.app_context():
#         db.drop_all()
#     time.sleep(1)
#     server.terminate()

# exit()


# from my_app import create_app, db 
from modelos import Clientes
# import modelos
from init import app, db
import sys

def reset_database():
    # app = create_app()
    
    with app.app_context():
        # 1. Drop all, deleta tudo
        db.drop_all()
        
        # 2. Recria tudo novamente
        db.create_all()
        
        print("Banco de dados limpo.")

def criar_db():
    with app.app_context():
        db.create_all()  # crias as tabelas

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        if (sys.argv[1] == "init"):
            criar_db()
    else:
        reset_database()