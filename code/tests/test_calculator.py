from carbon_calculator import calculate

def test_transport():
    result = calculate(500,250,2,"vegetarian")
    assert result["transport_co2"] == 96
