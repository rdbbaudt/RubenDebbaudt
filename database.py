from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                      connect_args={
                        'ssl':{
                          'ssl_ca': '/etc/ssl/cert.pem'
                        }
                      })

def parse_data(result):
  rows = result.fetchall()
  if len(rows) == 0:
    return None
  else:
    column_names = result.keys()
    return [dict(zip(column_names, row)) for row in rows]

def load_all_experiences_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM experiences")
    )

    return parse_data(result)

def load_experience_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM experiences WHERE id = :val"), 
            {'val': id}
        )
      
        return parse_data(result)

if __name__ == '__main__':
  print('Unit tests inserted here in future.')