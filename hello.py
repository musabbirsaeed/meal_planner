from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Yahoo! is an American web services provider headquartered in Sunnyvale, California, and owned by Verizon Media. The original Yahoo! company was founded by Jerry Yang and David Filo in January 1994 and was incorporated on March 2, 1995. Yahoo was one of the pioneers of the early Internet era in the 1990s  World!</h1>'
