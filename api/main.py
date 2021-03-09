from flask import Flask, json

transactions = [{ greenIndex: -42, targetName: "OMV Stinkstraße 32", IBAN:"AT123453453452234", amount: "2 Millionen Euro", purpose: "", buchungsdatum: "heute" }, { greenIndex: "over 9000", targetName: "Green Company: Pflanze zwei Bäume", IBAN: "AT89498239823", amount: "60 cent", purpose: "Ich liebe die Natur!!!", buchungsdatum: "gestern" }]

api = Flask(__name__)

@api.route('/getGreenTransactions', methods=['GET'])
def get_transactions():
  return json.dumps(transactions)

if __name__ == '__main__':
    api.run()