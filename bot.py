from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "🤖 Bot de Mercado Libre funcionando"

@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json()
    message = data.get("message", "⚠️ Mensaje vacío")

    # Aquí podrías conectar con Telegram
    print("Mensaje recibido:", message)

    return jsonify({"status": "ok", "message": message})

if __name__ == "__main__":
    # MUY IMPORTANTE: esto mantiene el proceso escuchando
    app.run(host="0.0.0.0", port=8080)
