from vehicle import vehicle_details

def test_vehicle_details():
    expected_output = (
        f"Vehicle ID: KA25E0001\n"
        f"Vehicle Name: Hero\n"
        f"Price: 50000\n"
        f"YOP: 2024\n"
    )

    assert vehicle_details("KA25E0001", "Hero", 50000, 2024)