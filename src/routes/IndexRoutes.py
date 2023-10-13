from flask import Blueprint, render_template, request, jsonify
import traceback

#Logger
from src.utils.Logger import Logger as log

main = Blueprint('index_blueprint', __name__)

@main.route("/")
def inicio():
    try:
        log.add_to_log("info", "{} {}".format(request.method, request.path))
        return render_template("index.html")
    except Exception as e:
        log.add_to_log("error", str(e))
        log.add_to_log("error", traceback.exec())
        
        response = jsonify({'message': "Internal Server Error", 'sucess': False})
        return response, 500