import importlib
from app import create_app

config_name = importlib.import_module('config').app_active
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
