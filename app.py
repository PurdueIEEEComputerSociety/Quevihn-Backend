from flask import Flask
from flask import request
import json
import mysql.connector

#####
# Database Schemas
# Database Name: quevihn
#
# Table: account
# Schema
# Primary Key: username
# userid, username, firstname, lastname, age
#
#
# Table: symptoms
# Schema
# Primary Key: userid
# userid, fever, headache
####

app = Flask(__name__)


@app.before_first_request  # Before the first user is able to do anything.
def initialize_db():
    hostID = '104.236.78.128'
    user = ''
    password = ''
    database = 'quevihn'
    # NOTE: This is a major security flaw. also, we never close the connection... Should also probably wrap in try except
    global cnx
    cnx = mysql.connector.connect(
    user=user, password=password, host=hostID, database=database)
    global cursor
    cursor = cnx.cursor()


@app.route("/")
def hello():
    return "Hello World!"



@app.route("/data/<username>")
def get_data(username):
    return getSymptomsForUser(username)

# Returns Symptoms for username


def getSymptomsForUser(username):
    #	Get userID from username
    #query = 'SELECT * FROM {}'.format("account")
    ##cursor.execute(query)
    #for i in cursor:
     #   for index, j in enumerate(i):
     #       if j == username:
     #           userID = i[index - 1]
     #   else:
     #       raise ValueError("Unknown user.")

   # 'SELECT fever AND headache FROM symptoms WHERE account.userid = symptoms.userID'

    #	Get symptoms for userID
    query = 'SELECT * FROM account, symptoms WHERE username = \'{}\' AND account.userid = symptoms.userid'.format(username)
    cursor.execute(query)
    for i in cursor:
        data = i[6:]

    # Json of symptoms
    return json.dumps(data)

#	Returns a list of symptoms from a user profile


def grabSymptoms(json):
    return json.loads(json)['Symptoms']

# Allows app to be accesible from anywhere
app.run(host="0.0.0.0", port="5000")
