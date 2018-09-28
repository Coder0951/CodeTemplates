import pypyodbc
import csv

d = "\\\\ent.core.company.com\mit-city01\City Public\Folder\Folder\FileName.accdb;"

# MS ACCESS DB CONNECTION
pypyodbc.lowercase = False
conn = pypyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
    r"Dbq=" + d)

# OPEN CURSOR AND EXECUTE SQL
cur = conn.cursor()
a = ' * '
b = '"AQry"'
c = "SELECT" + a + "FROM " + b

print(c)
cur.execute(c)
res = cur.execute(c)
columnList = [tuple[0] for tuple in res.description]
print(columnList)
# OPEN CSV AND ITERATE THROUGH RESULTS
with open("\\\\ent.core.company.com\mit-city01\City Public\Folder\FileName.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Eval Date/Time', 'Date', 'Agent', 'User ID'])
    for counter, row in enumerate(cur.fetchall()):
        print(counter)
        writer.writerow(row)
cur.close()
conn.close()
