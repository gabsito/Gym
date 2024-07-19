# Define membership plans and additional features with costs
MEMBERSHIPS = {
    '1': {
        'name': 'Basic',
        'cost': 50
        },
    '2': {
        'name': 'Premium',
        'cost': 100
        },
    '3': {
        'name': 'Family',
        'cost': 150
        }
}

ADDITIONAL_FEATURES = {
    '1': {
        'name': 'Personal Training',
        'cost': 30,
        'type': 'Normal'
        },
    '2': {
        'name': 'Group Classes',
        'cost': 20,
        'type': 'Normal'
        },
    '3': {
        'name': 'exclusive facilities',
        'cost': 60,
        'type': 'Premium'
        },
    '4': {
        'name': 'specialized programs',
        'cost': 65,
        'type': 'Premium'
        }
}


def display_memberships():
    print("Available Membership Plans:")
    for membership, details in MEMBERSHIPS.items():
        print(f"{membership}: {details['name']} - Cost: ${details['cost']}")


def display_additional_features():
    print("Available Additional Features:")
    for feature, details in ADDITIONAL_FEATURES.items():
        print(
            feature+": "+details['name']
            + "- Cost: $"+str(details['cost'])+" - Type: "+details['type'])


def calculate_total_cost(
        membership_cost,
        features_cost,
        premium_features=False):
    total_cost = membership_cost + features_cost
    if premium_features:
        total_cost *= 1.15  # Apply 15% surcharge
    return total_cost


def apply_group_discount(total_cost, num_members):
    if num_members >= 2:
        total_cost *= 0.90  # Apply 10% discount
    return total_cost


def get_membership_cost(membership_plan):
    if membership_plan in MEMBERSHIPS:
        return MEMBERSHIPS[membership_plan]['cost']
    return 0


def get_feature_cost(features):
    total_cost = 0
    for feature in features:
        if feature == "":
            return 0
        if feature not in ADDITIONAL_FEATURES:
            print(f"Error: {feature} is not a valid additional feature.")
            total_cost = -1
            break
        else:
            total_cost += ADDITIONAL_FEATURES[feature]['cost']
    return total_cost


def main():
    error = True
    premium_features = False
    fifty_dsc = False
    twenty_dsc = False
    while error:
        # Display membership options
        membership_plan = ""
        while membership_plan == "":
            display_memberships()
            membership_plan = input("Select a membership plan: ")
            if membership_plan not in MEMBERSHIPS:
                print("Error: Invalid membership plan.")
                membership_plan = ""

        # Validate and calculate costs
        membership_cost = get_membership_cost(membership_plan)

        # Display additional features
        selected_features = []
        features_cost = -1
        while features_cost == -1:
            display_additional_features()
            selected_features = input(
                "Select additional features (comma separated): ").split(',')
            selected_features = [
                feature.strip() for feature in selected_features]

            features_cost = get_feature_cost(selected_features)

        if features_cost > 0:
            premium_features = any(
                ADDITIONAL_FEATURES[feature_id]['type'] == 'Premium'
                for feature_id in selected_features)

        total_member_cost = calculate_total_cost(
            membership_cost,
            features_cost,
            premium_features)

        # Handle group discount
        num_members = int(input(
            "Enter the number of members signing up together: "))

        total_member_cost = apply_group_discount(
            total_member_cost,
            num_members)

        total_cost = total_member_cost*num_members
        if total_cost > 400:
            total_cost -= 50  # Apply $50 discount
            fifty_dsc = True
        elif total_cost > 200:
            total_cost -= 20  # Apply $20 discount
            twenty_dsc = True
        # Confirm membership
        selected_names = []
        if features_cost > 0:
            selected_names = [
                ADDITIONAL_FEATURES[feature_id]['name']
                for feature_id in selected_features]

        membership_name = MEMBERSHIPS[membership_plan]['name']
        print(f"Selected Membership: {membership_name}")
        print(f"Selected Features: {', '.join(selected_names)}")
        print("Applied Discounts: "
              + ("+15% surchage premium feature, " if premium_features else "")
              + ("-10% discount" if num_members >= 2 else "")
              + ("-$50 discount, " if fifty_dsc else "")
              + ("-$20 discount, " if twenty_dsc else ""))
        print(
            f"Total member Cost: ${total_member_cost:.2f}" +
            ", Final Cost: $"+str(total_cost))

        confirm = input("Confirm membership (yes/no): ").lower()

        if confirm == 'yes':
            print(f"Membership confirmed! Total cost: ${total_cost:.2f}")
            return int(total_cost)
        else:
            print("Membership canceled! -1")
            error = True


if __name__ == "__main__":
    main()
