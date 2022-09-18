from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 334000, number2 = 3487000)

@app.route('/mult')
def number():
    var1, var2 = 15210, 45846898960
    return render_template('body.html', num1 = var1, num2 = var2, multiplication = var1*var2)




if __name__ == '__main__':
    app.run(debug=True)
