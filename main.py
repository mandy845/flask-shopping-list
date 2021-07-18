from flask import *


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def shoppingList():
    return render_template('shopping_list.html')


@app.route("/items", methods=['POST'])
def items():
    product_details = {
        "name": request.form['name'],
        "item_id": request.form['item id'],
        "quantity": request.form['quantity'],
        "price": request.form['price']
    }

    return render_template("items.html", product_details=product_details)


if __name__ == "__main__":
    app.debug = True
    app.run()