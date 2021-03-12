from flask import Flask, json, jsonify

transactions = [{"greenIndex": -42, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"},{"greenIndex": 90, "targetName": "Green Company: Pflanze zwei Bäume", "IBAN": "AT89498239823", "amount": "60 cent", "purpose": "Ich liebe die Natur!!!", "buchungsdatum": "gestern"},{"greenIndex": -2, "targetName": "OMV ", "IBAN":"AT1234534534234", "amount": "2 MilEuro", "purpose": "", "buchungsdatum": "heute"}, {"greenIndex": -35, "targetName": "OStink 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"}, {"greenIndex": 93, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"}, {"greenIndex": -89, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"},{"greenIndex": 5, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"},{"greenIndex": 8, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"},{"greenIndex": 50, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"},{"greenIndex": 28, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"},{"greenIndex": 12, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"},{"greenIndex": -76, "targetName": "OMV Stinkstraße 32", "IBAN":"AT123453453452234", "amount": "2 Millionen Euro", "purpose": "", "buchungsdatum": "heute"}]

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