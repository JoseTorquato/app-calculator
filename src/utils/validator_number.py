def validator_number(number: str) -> any:
    print(number)
    if float(number):
        return float(number)
    else:
        raise Exception(f"\tO valor digitado não é um número real.")
