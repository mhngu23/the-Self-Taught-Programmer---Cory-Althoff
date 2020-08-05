list1 = ["Top Gun","Risky Business","Minority Report","1","2","3"]
print(list1)
import csv
with open("st.csv", "w") as f:
        w = csv.writer(f, delimiter=",")
        for row in list1:
            w.writerow(row)
