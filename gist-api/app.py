from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/<user>', methods=['GET'])
def get_user_gists(user):
    """Fetch and return public gists for specified GitHub user."""
    url = f"https://api.github.com/users/{user}/gists"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx
        gists = response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            # User not found → return empty list
            return jsonify({'user': user, 'gists': []})
        else:
            return jsonify({'error': f'HTTP error: {str(e)}'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch gists: {str(e)}'}), 500

    # Return simplified list with key details
    gist_list = []
    for gist in gists:
        gist_info = {
            'id': gist['id'],
            'description': gist.get('description', 'No description'),
            'public': gist['public'],
            'url': gist['html_url'],
            'files': list(gist['files'].keys()),
            'created_at': gist['created_at']
        }
        gist_list.append(gist_info)
    return jsonify({'user': user, 'gists': gist_list})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
