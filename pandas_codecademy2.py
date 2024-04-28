import pandas as pd

ad_clicks = pd.read_csv(r"C:/Users/nithi/Desktop/Data/csv/ad_clicks.csv")
print(ad_clicks.head())
print(ad_clicks.columns.tolist())

print(ad_clicks.groupby(['utm_source']).user_id.count())

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

print(clicks_by_source)

clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()

clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] +
    clicks_pivot[False])

print(clicks_pivot)
print(clicks_pivot.reindex(['utm_source', True, False, 'percent_clicked'], axis=1))

print(ad_clicks.groupby(['experimental_group']).user_id.count())

print(ad_clicks.groupby(['experimental_group','is_click']).user_id.count())

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

print(a_clicks)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

print(b_clicks)


a_clicks_group = a_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index()

print(a_clicks_group)

b_clicks_group = b_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index()

print(b_clicks_group)

clicks_group = ad_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index()

print(clicks_group)

clicks_group_pivot = clicks_group.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()

print(clicks_group_pivot.reindex(['experimental_group', True, False], axis=1))

clicks_group_pivot['percent_clicked'] = round(clicks_group_pivot[True] / (clicks_group_pivot[False] + clicks_group_pivot[True])*100, 2)

print(clicks_group_pivot)