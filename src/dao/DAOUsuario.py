import pymysql

class DAOUsuario:

    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",database="proyecto_db")

    def read(self,id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM productos order by descripcion")
            else:
                cursor.execute("SELECT * FROM productos where codigo = %s order by descripcion",(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO productos(descripcion, precio, stock, categoria) VALUES(%s,%s,%s,%s)",(data['descripcion'], data['precio'], data['stock'], data['categoria'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def update(self,id,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE productos SET descripcion=%s, precio=%s, stock=%s, categoria=%s where codigo = %s",(data['descripcion'], data['precio'], data['stock'], data['categoria'], id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self,id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("delete from productos where codigo = %s",(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
