import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')

class abcHandler(webapp2.RequestHandler):
    def get(self):
        colorful_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Colorful Response</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    background-color: #f0f8ff;
                    color: #2c3e50;
                }
                h1 {
                    font-size: 48px;
                    color: #e74c3c;
                    text-shadow: 2px 2px 4px #000000;
                }
                p {
                    font-size: 24px;
                    color: #3498db;
                }
            </style>
        </head>
        <body>
            <h1>Welcome!</h1>
            <p>abc!</p>
        </body>
        </html>
        """
        self.response.write(colorful_html)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Home Page!')

class CalculatorHandler(webapp2.RequestHandler):
    def get(self):
        calculator_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Calculator</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    background-color: #eafaf1;
                }
                h1 {
                    color: #4CAF50;
                }
                .calculator {
                    margin: auto;
                    width: 300px;
                    padding: 10px;
                    border: 2px solid #4CAF50;
                    border-radius: 10px;
                    background-color: #ffffff;
                }
                input[type="text"] {
                    width: 95%;
                    padding: 10px;
                    margin: 10px 0;
                    font-size: 16px;
                }
                input[type="button"] {
                    width: 22%;
                    padding: 10px;
                    margin: 5px 1%;
                    font-size: 16px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="button"]:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h1>Calculator</h1>
            <div class="calculator">
                <form name="calculator">
                    <input type="text" id="display" readonly>
                    <br>
                    <input type="button" value="1" onclick="addToDisplay('1')">
                    <input type="button" value="2" onclick="addToDisplay('2')">
                    <input type="button" value="3" onclick="addToDisplay('3')">
                    <input type="button" value="+" onclick="addToDisplay('+')">
                    <br>
                    <input type="button" value="4" onclick="addToDisplay('4')">
                    <input type="button" value="5" onclick="addToDisplay('5')">
                    <input type="button" value="6" onclick="addToDisplay('6')">
                    <input type="button" value="-" onclick="addToDisplay('-')">
                    <br>
                    <input type="button" value="7" onclick="addToDisplay('7')">
                    <input type="button" value="8" onclick="addToDisplay('8')">
                    <input type="button" value="9" onclick="addToDisplay('9')">
                    <input type="button" value="*" onclick="addToDisplay('*')">
                    <br>
                    <input type="button" value="C" onclick="clearDisplay()">
                    <input type="button" value="0" onclick="addToDisplay('0')">
                    <input type="button" value="=" onclick="calculate()">
                    <input type="button" value="/" onclick="addToDisplay('/')">
                </form>
            </div>
            <script>
                function addToDisplay(value) {
                    document.getElementById('display').value += value;
                }
                function clearDisplay() {
                    document.getElementById('display').value = '';
                }
                function calculate() {
                    try {
                        let result = eval(document.getElementById('display').value);
                        document.getElementById('display').value = result;
                    } catch (error) {
                        document.getElementById('display').value = 'Error';
                    }
                }
            </script>
        </body>
        </html>
        """
        self.response.write(calculator_html)

# Combine all routes into a single WSGIApplication
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/abc', abcHandler),
    ('/home', HomeHandler),
    ('/calculator', CalculatorHandler),
], debug=True)
