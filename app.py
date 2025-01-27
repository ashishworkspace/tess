import os, sys
from flask import Flask
import views

app = Flask(__name__)
app.add_url_rule("/", view_func = views.root, methods=['GET'])
app.add_url_rule("/read_ocr", view_func = views.read_ocr, methods=['POST'])
print("Server Ready", flush=True)

if __name__ == "__main__":    
    port = os.environ.get('PORT', 4000)
    app.run(debug=False, host='0.0.0.0', port=port)