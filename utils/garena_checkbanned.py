import requests as request
from utils.get_headers import get_headers
from utils.get_printColored import prRed, prGreen

baseUrl = "https://ff.garena.com/api/antihack/check_banned"

def fetch_checkbanned(uid: str) -> bool | None:
    if not uid or not uid.isdigit():
        prRed(f"Error: Invalid UID format '{uid}'. Free Fire UIDs must be numeric.")
        return None
    
    try:
        headers = get_headers()
        params = {"uid": uid}
        response = request.get(baseUrl, headers=headers, params=params)

        if response.ok:
            resJson = response.json()

            if resJson.get("status") == "success" and "data" in resJson:
                data = resJson["data"]
                is_banned = data.get("is_banned")

                if is_banned == 1:
                    prRed(f"[BANNED] UID {uid} is banned!")
                    return True
                elif is_banned == 0:
                    prGreen(f"[CLEAN] UID {uid} is not banned.")
                    return False
                
            elif resJson.get("status") == "error" and "msg" in resJson:
                msg = resJson.get("msg")

                if msg == "T_P_WRONG_ACCOUNT":
                    prRed(f"[ERROR] Account UID {uid} does not exist or is invalid.")
                    return None

        else:
            prRed(f"Failed to fetch data. Server responded with status code: {response.status_code}")
            return None
        
    except request.exceptions.RequestException as e:
        prRed(f"An error occurred while connecting to the API: {e}")
        return None