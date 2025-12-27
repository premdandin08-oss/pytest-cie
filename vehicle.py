def vehicle_details(vid, vname, price, yop):
    result = (
        f"Vehicle ID: {vid}\n"
        f"Vehicle Name: {vname}\n"
        f"Price: {price}\n"
        f"YOP: {yop}\n"
    )
    return result

if __name__ == "__main__":
    vid = "KA25E0001"
    vname = "Hero"
    price = 50000
    yop = 2024

    print(vehicle_details(vid, vname, price, yop))
