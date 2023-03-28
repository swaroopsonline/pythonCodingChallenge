# ---------------------------------- Date: 28 March 2023 ---------------------------------------------
# ----------------- The below code shows how to print in a reverse order from a Python Array --------

import numpy as np

print("----------------------NumPy Array -------------------------")

arr1 = np.array(["Fiat", "Maruti", "Volvo","Logan","Hyundai"])

i = len(arr1)
j = i - 1

for i in range(len(arr1)):

    print(arr1[j])
    j = j - 1






