from flask import jsonify



def responde(status,error,message,data):
    responseObject = {
        "error": error,
        "message": message,
        "data": data
    }

    return jsonify(responseObject), status