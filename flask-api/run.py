import os
from app import app

if __name__== "__main__":
    
    config_name = os.getenv('FLASK_ENV')
    app = create_app(config_name)
    app.run(debug=True)