from flask import Flask
import sys
from banking.logger import logging
from banking.exception import BankingException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        banking = BankingException(e,sys)
        logging.info(banking.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)