from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    todos_text = jsonify(todos)

    return todos_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()

    if 'label' not in request_body or 'done' not in request_body:
        print("ERROR: Missing required fields")
        return jsonify({"error": "Missing required fields"})

    todos.append(request_body)
    print("Incoming request with the following body:", request_body)
    
    return jsonify(todos)

# @app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position):
#     if 0 <= position < len(todos):
#             deleted_todo = todos.pop(position)
#             print("This is the position to delete:", position)
#             return {"message": "Todo deleted successfully", "deleted_todo": deleted_todo}, 200
#     else:
#             return {"error": "Invalid position"}, 400 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

        if 0 <= position < len(todos):
            todos.pop(position) 
            return jsonify(todos), 200
        else:        
            return jsonify({"error": "Invalid position"}), 400

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)