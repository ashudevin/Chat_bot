from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency =  data['queryResult']['parameters']['currency-name']
    
    print(source_currency, amount, target_currency) 
    cf = fetch_currency_details(source_currency, target_currency)
    final = cf * amount
    final = round(final, 2)
    
    response = {
        "fulfillmentText":"{} {} is {} {}".format(amount, source_currency, final, target_currency)
    }

    return jsonify(response)

def fetch_currency_details(source, target):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_YEWJqCkUs2qqcmm7kBBBwLHh22usJJyZ6Aao0HcF&currencies={}&base_currency={}".format(target, source)

    response = requests.get(url)
    response = response.json()
    cal = (response['data'][target])
    return cal

    # return response["{}, {}".format(source, target)]

  
if __name__ == "__main__":
    app.run(debug=True)

