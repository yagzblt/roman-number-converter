from flask import Flask, render_template, request

app = Flask(__name__)

val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


print("###  This program converts decimal numbers to Roman Numerals ###")
print('(To exit the program, please type "exit")')

while True:
    user_input = input("Please enter a number between 1 and 3999, inclusively: ")

    # Check for exit
    if user_input.lower() == "exit":
        break

    # Validate input
    try:
        num = int(user_input)
        if 1 <= num <= 3999:
            # Convert and display result
            roman_num = ''
            for i in range(len(val)):
                while num >= val[i]:
                    roman_num += syb[i]
                    num -= val[i]
            print(f"The Roman numeral representation: {roman_num}")
        else:
            print("Input out of range. Please enter a number between 1 and 3999.")
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to end the program.")


@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']
        if not alpha.isdecimal():
            return render_template('index.html', developer_name='murat', not_valid=True)
        number = int(alpha)
        if not 0 < number < 4000:
            return render_template('index.html', developer_name='murat', not_valid=True)
        return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='murat')
    else:
        return render_template('index.html', developer_name='murat', not_valid=False)



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
