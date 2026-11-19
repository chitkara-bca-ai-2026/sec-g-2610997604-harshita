tution_fee=float(input("Enter Tution Fee: "))
lab_fee=float(input("Enter Lab Fee: "))
library_fee=float(input("Enter Library Fee: "))
exam_fee=float(input("Enter Exam Fee: "))
discount_amount=float(input("Enter Discount Amount: "))

print(f"Tution Fee: ", tution_fee)
print(f"Lab Fee: ", lab_fee)
print(f"Library Fee: ", library_fee)
print(f"Exam Fee: ", exam_fee)

total_fee= tution_fee+ lab_fee+ library_fee+ exam_fee
print("Total Fee: ", total_fee)
fee_after= total_fee-discount_amount
print("Fee after Discount: ", fee_after)
annual= fee_after*2
print("Annual Fee: ", annual)
installment= annual//12
print("Monthly Installment: ", installment)
