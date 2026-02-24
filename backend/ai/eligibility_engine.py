def evaluate_rule(user_data, rule):
    field = rule["field"]
    op = rule["op"]
    value = rule["value"]

    if field not in user_data or user_data[field] is None:
        return False, f"{field} missing"

    user_value = user_data[field]

    if op == "<":
        return user_value < value
    if op == "<=":
        return user_value <= value
    if op == ">":
        return user_value > value
    if op == ">=":
        return user_value >= value
    if op == "==":
        return user_value == value

    return False


def check_eligibility(user_data, scheme):
    for rule in scheme["rules"]:
        if not evaluate_rule(user_data, rule):
            return False

    return True