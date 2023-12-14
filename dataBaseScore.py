import sqlite3

with sqlite3.connect("score_data_base.db") as conexion:
    try:
        sentencia = '''
                    create table Scores
                    (
                    id integer primary key autoincrement,
                    nombre text,
                    score int,
                    coins int
                    


                    )


                    '''
        sentencia = '''
                   insert into Scores(nombre,score,coins) values()

                    '''
        conexion.execute(sentencia)
    except Exception as e:
        print(f"Error: {e}")

#select * from Scores order by score desc