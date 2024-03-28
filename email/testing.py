summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),

    'The {} had the most sales: {}'.format(most, x),

    ('The most popular year was {} with {} sales'.format(most_popular_sales[0][0], most_popular_sales[0][1]))

  ]

x = "/n".join(summary)
print(x)