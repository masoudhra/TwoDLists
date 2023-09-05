queb_list = [
    [2, 3, 3],
    [4, 8, 2],
    [3, 5, 4]
]

# elemane avale liste dovom az queb_list
print(queb_list[1][0])


# hajme mokaab
for queb in queb_list:
    result = 1
    for dimension in queb:
        result = result * dimension

    print(result)