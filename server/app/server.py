from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
def square_root():
    n = 49 

    result = n**0.5
    # Create an HTML response with the result
    html_response = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Square Root </title>
        </head>
        <body>
            <h3>The square root of {n} is: {result}</h3>
            
        </body>
        </html>
    '''
    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
