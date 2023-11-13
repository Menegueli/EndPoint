from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Endpoint que retorna posts da API JSONPlaceholder
@app.route('/api/posts', methods=['GET'])
def get_posts():
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Verifica se houve algum erro na requisicão
        posts = response.json()
        return jsonify(posts)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
