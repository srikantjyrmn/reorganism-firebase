import firebase_functions as functions

@functions.https_on_call()
def chat(req: functions.Request) -> functions.Response:
    try:
        data = req.data
        message = data.get('message', '')
        response = f"Yes, I heard: {message}"
        return functions.Response(response)
    except Exception as e:
        print(f"Error in chat function: {str(e)}")
        return functions.Response({"error": str(e)}, status=500)