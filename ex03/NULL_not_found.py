def NULL_not_found(object: any) -> int:
    try:
        if type(object) is type(None):
            print(f"Nothing: {object} " f"{type(object)}")
        elif type(object) is float and object != object:
            print(f"Cheese: {object} {type(object)}")
        elif type(object) is int and not object:
            print(f"Zero: {object} {type(object)}")
        elif type(object) is str and not object:
            print(f"Empty: {object} {type(object)}")
        elif type(object) is bool and object is False:
            print(f"Fake: {object} {type(object)}")
        else:
            raise Exception("Type not Found")
        return 0
    except Exception as inst:
        print(inst)
        return 1
