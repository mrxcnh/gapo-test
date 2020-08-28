def calc(formula: str, data: dict) -> float:
    for i in data.keys():
        formula = formula.replace(i, str(data[i]))
    return eval(formula)


if __name__ == "__main__":
    data = {
        "price": 100,
        "amount": 50,
        "discount": 0.5,
        "unit": 1000,
        "added_tax": 50000,
    }

    print(calc("price * amount * discount", data))
