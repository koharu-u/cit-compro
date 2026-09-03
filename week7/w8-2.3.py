joongBaey = [[ 120, 80,  350, 200 ],
             [ 240, 200, 100, 300 ],
             [ 300, 200, 400, 380 ],
             [ 500, 100, 380, 50  ]]
Branch = ["สาขา A", "สาขา B", "สาขา C", "สาขา D" ]
Model  = ["iPhone 12", "Samsung Galaxy Note20", "Sony Xperia 1 II", "HTC U11 Plus" ]
b = 0
m = 2

# ---- SNIP ----

for i_model in range(len(joongBaey)):
    if (joongBaey[i_model][m] > joongBaey[b][m]):
        b = i_model

# ---- SNIP ----
print(Branch[b],"ขายสมาร์ทโฟนรุ่น",Model[m],"ได้สูงสุด")
