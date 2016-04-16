#!/usr/bin/env python

from flask import Flask
from emitter import emit_donation, emit_subscription
app = Flask(__name__)


@app.route('/donation/')
def receive_donation():
    emit_donation({
        "username": "singlerider",
        "amount": 45,
        "currency": "USD",
        "message": "GREAT JOB!"
    })
    return 'Donation!'


@app.route('/subscription/')
def receive_subscription():
    emit_subscription({
        "username": "singlerider",
        "months": 5
    })
    return 'Subscription!'

if __name__ == '__main__':
    app.run()
