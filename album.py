from flask import Flask
from datos import album,sobre, Prestamo
import json
import random
app =   Flask(__name__)
def __init__(self):
        self = []
        self.prestamistas = []
        self.prestamos = []

if __name__ == '__main__':
    app.run(debug=True, port=4000)

def getCustomer(self):
        self.search_customers = [customer for customer in self.prestamistas]
        temporal = []
        for i in self.search_customers:
            tmpDict = {'cui':i.cui,'first_name':i.first_name,'last_name':i.last_name,'record':self.getRecord(i.cui)}
            temporal.append(tmpDict)
        return json.dumps(temporal),200
