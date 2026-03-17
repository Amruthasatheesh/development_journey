#Task 24 || Nested list || 26-02-2026

products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]

# 1. display all product names
# 2. product with the highest price
# 3. display electronics products
# 4. display products where the brand is Apple
# 5. which category has most products
# 6. product with maximum stock
# 7. list all categories
all_product_names=[lst for lst in products]
print(all_product_names)
pro_withhighest_price=max([lst[4]for lst in products ])
product_high_price=[lst[1]for lst in products if lst[4]==pro_withhighest_price]
print(product_high_price)
electronic_products=[lst[1]for lst in products if lst[3]=="Electronics"]
print(electronic_products)
apple_brand=[lst[1]for lst in products if lst[2]=="Apple"]
print(apple_brand)
# most_products_category=max([lst[3] for lst in products if lst[3]=="Electronics"])
# print(most_products_category)
# pro_mxm_stock=max([lst[5]for lst in products])
# product_mxm_stock=[lst[1]for lst in products if lst[5]==pro_mxm_stock]
# print(product_mxm_stock)
all_categories=[lst[3] for lst in products]
category_count={c:all_categories.count (c)for c in all_categories}
category_count_list=[[v,k]for k,v in category_count.items()]
print(sorted(category_count_list,reverse=True))

