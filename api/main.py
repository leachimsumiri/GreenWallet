#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from flask import Flask, json, jsonify
from obp.lib import obp

#@Stefan die Transaktionen kannst mal verwenden
obpTransactions = obp.getPublicTransactions
mockTransactions = '[{ greenIndex: -42, targetName: "OMV Stinkstraße 32", IBAN:"AT123453453452234", amount: "2 Millionen Euro", purpose: "", buchungsdatum: "heute" }, { greenIndex: "over 9000", targetName: "Green Company: Pflanze zwei Bäume", IBAN: "AT89498239823", amount: "60 cent", purpose: "Ich liebe die Natur!!!", buchungsdatum: "gestern" }]'

greenIndexRegex = [
    ('.*OMV.*',                       -42),
    ('.*green company.*',            9001),
    ('.*ALIAS.*',                    -100),
]

def greenLookup(search, checklist):
    for pattern, value in checklist:
        if re.search(pattern, search):
            return value
    return None

api = Flask(__name__)
@api.route('/getGreenTransactions', methods=['GET'])
# @cross_origin() # for POST / PUT / etc.
def get_transactions():
    
    # Get Banking Data 
    # TODO: For future Versions should take different/varying accounts!
    bankData = obpTransactions()

    greenish = [{
        'greenIndex':       greenLookup(ta['other_account']['holder']['name'], greenIndexRegex),
        'buchungsDatum':    ta['details']['completed'], 
        'targetName':       ta['other_account']['holder']['name'],
        'IBAN':             ta['other_account']['IBAN'],
        'amount':           ta['details']['value']['currency'] + ' ' + ta['details']['value']['amount'],
        'purpose':          ta['details']['description'],
        } for ta in bankData['transactions']]
    response = jsonify(greenish)

    # Temp Test / Mock Response
    # print(json.dumps(greenish, indent=2, sort_keys=True))
    # response = jsonify(bankData)
    # response = jsonify(mockTransactions)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == '__main__':
    # print(json.dumps(obpTransactions(), indent=2, sort_keys=True))
    api.run()