joongBaey = [[ 120, 80,  350, 200 ],
             [ 240, 200, 100, 300 ],
             [ 300, 200, 400, 380 ],
             [ 500, 100, 380, 50  ]]
Branch = ["สาขา A", "สาขา B", "สาขา C", "สาขา D" ]
Model  = ["iPhone 12", "Samsung Galaxy Note20", "Sony Xperia 1 II", "HTC U11 Plus" ]
s = 0

for m in range(len(joongBaey)):
    s = s + joongBaey[m][0]

print("ยอดขายรวมสมาร์ทโฟนรุ่น",Model[0],"ของทุกสาขามียอดเท่ากับ",s,"เครื่อง")
