from fooditem import fooditemcw

def create_grocery_listcw():
    grocery = []
    item_number = int(input("Please input number of items: "))
    if item_number >= 1:
        for _ in range(item_number):
            name = str(input("Name of the item: "))
            quantity = float(input("Quantity of the item: "))
            if quantity > 0:
                item = fooditemcw(name, quantity)
                grocery.append(item)
    else:
        print("Please input correctly.")
        return create_grocery_listcw()
    return grocery

def print_receiptcw(grocery_list):
    total_costcw = 0
    for j in grocery_list:
        print(f"Food: {j._food}")
        print(f"Amount: {j._pounds} pounds")
        print(f"Standard Price per pound: ${j._standard:.2f}")
        print(f"Total Cost: ${j.costcw():.2f}")
        total_costcw += j.costcw()

def calculate_total_costcw(food_list):
    total_costcw = 0
    for food in food_list:
        total_costcw += food.costcw()
    return total_costcw

def main():
    food_list = create_grocery_listcw()
    print_receiptcw(food_list)
    total_cost = calculate_total_costcw(food_list)
    print(f"Total cost of all items: ${total_cost:.2f}")

if __name__ == "__main__":
    main()