import project
from api import api_bp
from views import views

if __name__ == '__main__':
    project.app.register_blueprint(api_bp, url_prefix='/api')
    project.app.register_blueprint(views)
    project.app.run(host='0.0.0.0', port=80, debug=True)




