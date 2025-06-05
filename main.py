from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    teste = [
        {
            'id':1,
            'capa-filme': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT1BmFVF5tHZXQvckmvknsP2BOfIwiW6XFlnq7S3QuPUIQJhkJ75O6y1xF0HjlyYjrY8yLycfjlp1fBFc7XB2OOHEAbh23NnLcEmvs4wXA',
            'nome': 'Assim na Terra como no inferno',
            'sinopse': 'Scarlett Marlowe (Perdita Weeks), uma jovem especialista em alquimia, continua o trabalho de seu falecido pai em busca da pedra filosofal, uma substância lendária capaz de transformar metal em ouro e garantir a vida eterna, descoberta por Nicolas Flamel. Após achar a “Chave Rosa” em uma caverna no Irã, ela viaja para Paris em busca da ajuda de George (Ben Feldman), sua antiga paixão que foi abandonado por ela em uma prisão Turca enquanto ia atrás da pedra. Junto com Benji (Edwin Hodge) o cameraman, eles traduzem a lápide de Flamel, que contém um enigma que os guia para as catacumbas de Paris.',
            'nota':1,
            'dia-assistido': 1,
            'duracao': '1:33',
        }
    ]
    return jsonify(teste)

if __name__ == '__main__':
    app.run(debug=True)
