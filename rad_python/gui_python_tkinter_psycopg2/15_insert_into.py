import psycopg2
conn = psycopg2.connect(database = "postgres", user="postgres" , password="0000" , host="127.0.0.1", port="5432") # LEMBRAR SENHA
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""INSERT INTO public."agenda" ("id", "nome" , "telefone") VALUES (1, 'Pessoa 1' , '02199999999')""") 
conn.commit() 
print("Inserção realizada com sucesso!"); 
conn.close()