import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route("/cavalo")
def horse():
    return "<h1>Oxi ta fazendo oq aq?</h1>"

def init_db():
    with sqlite3.connect("database.db") as conn:

        conn.execute("""
        CREATE TABLE IF NOT EXISTS RDR(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            funcão TEXT NOT NULL,
            montaria TEXT NOT NULL,
            mandato TEXT NOT NULL,
            situacão TEXT NOT NULL,
            imagem_url TEXT NOT NULL
            )
        """)
init_db()

@app.route("/rdr", methods=["POST", "PUT"])
def rdr2():
    
    rdr2 = request.get_json()
    
    nome = rdr2.get("nome")
    funcão = rdr2.get("funcão")
    montaria = rdr2.get("montaria")
    mandato = rdr2.get("mandato")
    situacão = rdr2.get("situacão")
    imagem_url = rdr2.get("imagem_url")
    if request.method == "POST":
        if not nome or not funcão or not montaria or not situacão or not imagem_url:
            return jsonify({"erro":"todos os campos são obrigatorios"}), 400
    
        with sqlite3.connect("database.db") as conn:
            conn.execute(f"""
        INSERT INTO RDR (nome, funcão ,montaria, mandato, situacão, imagem_url)
        values ("{nome}", "{funcão}", "{montaria}", "{mandato}", "{situacão}", "{imagem_url}")
        """)
        conn.commit()
        return jsonify({"mensagem":"personagem cadastrado"}), 201
    elif request.method == "PUT":

  
        with sqlite3.connect("database.db") as conn:
            conn.execute(f"""
                UPDATE RDR SET nome = "{nome}",
                funcão = "{funcão}",
                montaria = "{montaria}",
                mandato = "{mandato}",
                situacão = "{situacão}",
                imagem_url = "{imagem_url}"
              """
            )   
            conn.commit()
            return jsonify({"mensagem": "personagem atualizado com sucesso"}), 200

@app.route("/rdr2", methods=["GET"])
def Van_Der_Linder():
    with sqlite3.connect("database.db") as conn:
        rdr = conn.execute("SELECT * FROM RDR").fetchall()

        gangue = []

        for item in rdr:
            dicionario_rdr={
                "id": item[0],
                "nome": item[1],
                "funcão": item[2],
                "montaria": item[3],
                "mandato": item[4],
                "situacão": item[5],
                "image_url": item[6]
            }
            gangue.append(dicionario_rdr)
    return jsonify(gangue), 200




if __name__ == "__main__":
    app.run(debug=True)