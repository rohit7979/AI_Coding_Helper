


# import google.generativeai as genai
# import os

# api_key ="AIzaSyA898GT7Xy0QlGmEwPXnNbKhcPGZg3FW9Q"; 
# genai.configure(api_key=api_key)

# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content("Write a Python function to calculate factorial")
# print(response.text)


from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Google Generative AI
api_key = "AIzaSyA898GT7Xy0QlGmEwPXnNbKhcPGZg3FW9Q"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/suggest-code', methods=['POST'])
def suggest_code():
    data = request.get_json()  # Get JSON data from the request
    code = data.get('code')  # Extract the code field from the JSON data
    if not code:
        return jsonify({'error': 'No code provided'}), 400
    
    try:
        # Generate content based on the provided code
        response = model.generate_content(f"Suggest an improvement or addition to the following JavaScript code: {code}")
        suggestion = response.text
        return jsonify({'suggestion': suggestion})  # Return the suggestion as a JSON response
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message if something goes wrong

if __name__ == '__main__':
    app.run(debug=True, port=3000)  # Run the Flask application on port 3000
