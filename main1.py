from supabase import create_client
from fastapi import FastAPI
app = FastAPI()



supabase_url="https://xudfyfixsopxdvckutpz.supabase.co"
supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh1ZGZ5Zml4c29weGR2Y2t1dHB6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MDI1MjU0MywiZXhwIjoyMDY1ODI4NTQzfQ.mw-1sBphrXiZAbAaLY0JJX3oy8-uVSi3wXEp03yeeV0"
# supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh1ZGZ5Zml4c29weGR2Y2t1dHB6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAyNTI1NDMsImV4cCI6MjA2NTgyODU0M30.sdxyyi5rYgtHdYapYBy9KKi0HZKmZ3QJHwvfJLiCpXE"
database = create_client(supabase_url,supabase_api_key)


@app.post("/login")
def login(username,password):
    print(username, password)
    result = database.table("app_users").select("*").eq('user_name',username).eq("password",password).execute()
    print(result.data)
    if result.data:
        return True
    else:
        return False



@app.get("/users")
def read_users():
    result = database.table("app_users").select('id,name').execute()
    return result.data

@app.get('/create')
def create_user(name,age,password):
    result = database.table('app_users').insert({'name':name,
                                        'age':age,
                                        'password':password}).execute()
    
    return result.data
