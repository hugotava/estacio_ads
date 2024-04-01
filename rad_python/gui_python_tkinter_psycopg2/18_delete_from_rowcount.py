import psycopg2
conn = psycopg2.connect(database = "postgres", user="postgres" , password="0000" , host="127.0.0.1" , port="5432" ) #LEMBRAR SENHA
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""DELETE FROM public."agenda" WHERE "id"=1""") 
conn.commit() 
cont=cur.rowcount 
print(cont, "Registro excluído com sucesso!") 
print("Exclusão realizada com sucesso!"); 
conn.close()