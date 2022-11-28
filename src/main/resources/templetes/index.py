from flask_restful import Resource, Api
from email import message
import webbrowser

class Index(Resource):
    f =open("1.html","w")
    message='''
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale = 1.0">
            <title>FLASK API</title>
        </head>
        <body>
            <h1>Wellcome</h1>
        </body>
    </html>
    '''
    f.write(message)
    f.close
    webbrowser.open_new_tab("1.html")
