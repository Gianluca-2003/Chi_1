from database.DB_connect import DBConnect
from model.Track import Track


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_Tracks():
        cnx = DBConnect.get_connection()
        tracks = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """select t.*
                        from Track t """
            cursor.execute(query)
            for row in cursor:
                tracks.append(Track(**row))

            cursor.close()
            cnx.close()
        return tracks