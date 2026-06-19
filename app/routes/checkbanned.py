from flask import Blueprint, request, jsonify
from utils.garena_checkbanned import fetch_checkbanned 

checkbanned_bp = Blueprint("checkbanned", __name__)

@checkbanned_bp.route('/checkbanned', methods=['GET'])
def checkbanned():
    uid = request.args.get('uid')
    
    if not uid:
        return jsonify({
            "status": "error",
            "message": "Missing 'uid' query parameter."
        }), 400
        
    result = fetch_checkbanned(str(uid))
    
    if result is True:
        return jsonify({
            "uid": uid,
            "is_banned": True,
            "status": "banned"
        }), 200
        
    elif result is False:
        return jsonify({
            "uid": uid,
            "is_banned": False,
            "status": "clean"
        }), 200
        
    else:
        return jsonify({
            "status": "error",
            "message": f"Could not verify UID '{uid}'. It may not exist or the service is down."
        }), 404