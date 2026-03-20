while True:
    print("selected items:")
    items_name={
        1:"beef stew",
        2:"vegetable rice",
        3:"githeri",
        4:"shawarma",

    }
    for i,j in items_name.items():
        print(i,j)
    select_item=input("select the items:(1,5):")
    if select_item=="1":
        print("you selected beef stew:")
    elif select_item=="2":
        print("you selected vegetable rice:")
    elif select_item=="3":
        print("you selected githeri:")
    elif select_item=="4":
        print("you selected shawarma:")
    else:
        print("invalid selection:please try again:")



