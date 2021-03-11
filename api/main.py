from flask import Flask, json, jsonify

transactions = '[{ greenIndex: -42, targetName: "OMV Stinkstraße 32", IBAN:"AT123453453452234", amount: "2 Millionen Euro", purpose: "", buchungsdatum: "heute" }, { greenIndex: "over 9000", targetName: "Green Company: Pflanze zwei Bäume", IBAN: "AT89498239823", amount: "60 cent", purpose: "Ich liebe die Natur!!!", buchungsdatum: "gestern" }]'

api = Flask(__name__)

@api.route('/getGreenTransactions', methods=['GET'])
# @cross_origin()
def get_transactions():
    response = jsonify(transactions)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    # return json.dumps(transactions)

if __name__ == '__main__':
    api.run()