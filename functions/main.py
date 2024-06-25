from firebase_functions import https_fn
from firebase_admin import initialize_app


initialize_app()

@https_fn.on_call()
def chat(req: https_fn.CallableRequest) -> dict:
    try:
        data = req.data
        message = data.get('message', '')
        response = f"Yes, I heard: {message}"
        return {"result": response}
    except Exception as e:
        print(f"Error in chat function: {str(e)}")
        return {"error": str(e)}