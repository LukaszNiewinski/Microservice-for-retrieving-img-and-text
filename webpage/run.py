import project
from app import api_bp


if __name__ == '__main__':
    project.app.register_blueprint(api_bp, url_prefix='/api')
    project.app.run(host='0.0.0.0', port=80, debug=True)




