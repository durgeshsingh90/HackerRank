def solve(meal_cost, tip_percent, tax_percent):
  total = meal_cost + meal_cost*(tip_percent/100) + meal_cost* (tax_percent/100)
  return (int(round(total,0)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
