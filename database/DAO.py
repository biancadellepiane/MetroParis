from database.DB_connect import DBConnect
from model.fermata import Fermata
from model.connessione import Connessione

class DAO():

    @staticmethod
    def getAllFermate():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata"
        cursor.execute(query)

        for row in cursor:
            result.append(Fermata(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def hasConnessione(u: Fermata, v: Fermata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query =  """SELECT *
                    FROM connessione c 
                    WHERE c.id_stazP = %s and c.id_stazA = %s"""

        #prendo risposte da db
        cursor.execute(query, (u.id_fermata, v.id_fermata))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return len(result) > 0 #>0 almeno una connessione quindi aggiungo l'arco

    @staticmethod
    def getVicini(u: Fermata, v: Fermata):
        conn = DBConnect.get_connection()

        result = [] #lista di connesioni che partono dal nodo u

        cursor = conn.cursor(dictionary=True)
        query =  """select *
                    from connessione c
                    where c.id_stazP = 4"""

        cursor.execute(query, (u.id_fermata, v.id_fermata))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return len(result) > 0

    @staticmethod
    def getVicini(u: Fermata): #data solo una fermata
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        #data una stazione di partenza, trovo gli arrivi
        query = """SELECT *
                    FROM connessione c 
                    where c.id_stazP = %s"""

        cursor.execute(query, (u.id_fermata,))

        for row in cursor:
            result.append(Connessione(**row)) #** per scompattare i dizionari

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                     FROM connessione c 
                     """

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result