from mydb import updateDb
with updateDb('./comics.db') as sh:
    sh.execute("CREATE TABLE superhero(
               name text,
               power text,
               publisher text
               )")
