
from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("We are testing exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "Hey! this is CI/CD Pipeline 1"

if __name__=="__main__":
    app.run(debug=True)
