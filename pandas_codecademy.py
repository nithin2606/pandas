
import pandas as pd

inventory = pd.read_csv(r"C:/Users/nithi/Desktop/Data/csv/inventory.csv")
print(inventory.head(10))
# print(inventory)


staten_island = inventory.head(10)

product_request = staten_island.product_description


seed_request = lambda x: x if (x.location == 'Brooklyn' and x.product_type == 'seeds') else 'none'
# print(inventory.apply(seed_request, axis=1))
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
print(combine_lambda)
#
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory.head())
