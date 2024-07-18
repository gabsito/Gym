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
        print(f"{feature}: {details['name']} - Cost: ${details['cost']} - Type: ${details['type']}")


def calculate_total_cost(
        membership_cost, 
        features_cost, 
        premium_features=False):
    total_cost = membership_cost + features_cost
    if premium_features:
        total_cost *= 1.15  # Apply 15% surcharge
    if total_cost > 400:
        total_cost -= 50  # Apply $50 discount
    elif total_cost > 200:
        total_cost -= 20  # Apply $20 discount
    return total_cost


def main():
    # Display membership options
    membership_plan = ""
    while membership_plan == "":
        display_memberships()
        membership_plan = input("Select a membership plan: ")
        if membership_plan not in MEMBERSHIPS:
            print("Error: Invalid membership plan.")
            membership_plan = ""

    # Validate and calculate costs
    membership_cost = MEMBERSHIPS[membership_plan]['cost']

    # Display additional features
    selected_features = []
    while selected_features.__len__() <= 0:
        display_additional_features()
        selected_features = input("Select additional features (comma separated): ").split(',')
        selected_features = [feature.strip() for feature in selected_features]

        features_cost = 0
        for feature in selected_features:
            if feature not in ADDITIONAL_FEATURES:
                print(f"Error: {feature} is not a valid additional feature.")
                selected_features = []
            else:
                features_cost += ADDITIONAL_FEATURES[feature]['cost']

    premium_features = membership_plan == 'Premium'
    total_member_cost = calculate_total_cost(
        membership_cost,
        features_cost,
        premium_features)

    # Handle group discount
    num_members = int(input("Enter the number of members signing up together: "))
    if num_members >= 2:
        total_member_cost *= 0.90  # Apply 10% discount for group membership

    total_cost = total_member_cost*num_members

    # Confirm membership
    print(f"Selected Membership: {membership_plan}")
    print(f"Selected Features: {', '.join(selected_features)}")
    print(f"Total member Cost: ${total_member_cost:.2f}, Final Cost: ${total_cost:.2f}")
    confirm = input("Confirm membership (yes/no): ").lower()
    
    if confirm == 'yes':
        print(f"Membership confirmed! Total cost: ${total_cost:.2f}")
        return int(total_cost)
    else:
        print("Membership canceled.")
        return -1


if __name__ == "__main__":
    main()
