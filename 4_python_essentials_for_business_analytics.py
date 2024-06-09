# Task 1 Sales Data Cloning and Modification

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

import copy
weekly_sales_copy = copy.deepcopy(weekly_sales)

weekly_sales_copy["Week 2"]["Electronics"] = 18000

print(weekly_sales)
print(weekly_sales_copy)

'''
To create a deep copy I imported the copy module and then assigned copy.deepcopy(weekly_sales) to the new dictionary week_sales_copy
After creating this new deep copy I navigated inside the nested dictionary by going through the key "Week 2" and the nested dictionary's key "Electronics" to reassign the new value of 18000.
Lastly I printed both the original dictionary and the newly modified deep copy dictionary to show that the modification I had just made did not affect the original, meaning the deep copy was effective.
'''