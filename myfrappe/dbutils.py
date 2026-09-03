from pymongo import MongoClient
from pymongo.server_api import ServerApi
from supabase import create_client
import dns.resolver
import json
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, DateTime, func

dns.resolver.default_resolver = dns.resolver.Resolver(filename="/data/data/com.termux/files/usr/etc/resolv.conf")

def mdb_op():
  mng_uri = "mongodb+srv://asief:ib0rJu5gK7Tw5psB@cluster0.up6y7.mongodb.net/?appName=Cluster0"
  
  mng_client = MongoClient(mng_uri, server_api = ServerApi('1'))
  
  try: 
    mng_client.admin.command("ping")
    return ("MongoDB connected successfully")
  except Exception as e:
    return (e)
    

def psg_op():
  pg_url = "https://nrkfgubozcjiujdusruu.supabase.co"
  supa_client = create_client(pg_url)
  try:
    supa_client.auth.get_session()
    # return ("PostgreSQL connected successfully")
    pg_response = supa_client.table("asief_table").select("*").limit(1).execute()
    return json.dumps(pg_response.data)
  except Exception as e:
    return json.dumps({"error": str(e)})

def lite_op():
  engine = create_engine("sqlite:///myfrappe/db/accounting.db")
  
  metadata = MetaData()
  
  customers = Table(
    "customers_1", metadata,
    Column("id", Integer, primary_key=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now(),nullable=False),
    Column("name", String)
  )
  
  metadata.create_all(engine)
  
  new_row = Table("customers_1", metadata, autoload_with=engine)
  
  stmt = insert(customers).values(name="Asief")
  
  with engine.begin() as conn:
    conn.execute(stmt)
    
  
  
  
  
  try:
    with engine.connect() as conn:
      conn.execute(text("SELECT 1"))
      
  except Exception as e:
    return f"Connection failed: {e}"
  
  return ("SQLite connected successfully")

def mongo_listdb():
  return(client.list_database_names())
  

  
  