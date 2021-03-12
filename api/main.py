#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, json, jsonify

from obp.lib import obp

#@Stefan die Transaktionen kannst mal verwenden
obpTransactions = obp.getPublicTransactions
mockTransactions = '[{ greenIndex: -42, targetName: "OMV Stinkstraße 32", IBAN:"AT123453453452234", amount: "2 Millionen Euro", purpose: "", buchungsdatum: "heute" }, { greenIndex: "over 9000", targetName: "Green Company: Pflanze zwei Bäume", IBAN: "AT89498239823", amount: "60 cent", purpose: "Ich liebe die Natur!!!", buchungsdatum: "gestern" }]'

greenIndex = {
    'omv':                      -42,
    'green company':            9001,
}

api = Flask(__name__)
@api.route('/getGreenTransactions', methods=['GET'])
# @cross_origin()
def get_transactions():
    response = jsonify(mockTransactions)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    # return json.dumps(transactions)

if __name__ == '__main__':
    print(json.dumps(obpTransactions(), indent=4, sort_keys=True))
    api.run()