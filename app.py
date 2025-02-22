from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    #logging.info("we are testing logging module")
    #return "Starting Machine Learning MODELS And its Intution to get some predictions"

    try:
        raise Exception("we are testing Custome Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message) #error_massage
        logging.info("we are testing logging module")
    return "Starting Machine Learning MODELS And Practice"

if __name__=="__main__":
    app.run(debug=True)
