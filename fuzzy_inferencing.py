def fuzzy_membership(value, low, high):
    """Calculate membership using an increasing linear function."""
    if low >= high:
        raise ValueError("'low' must be smaller than 'high'.")

    if value <= low:
        return 0.0
    if value >= high:
        return 1.0

    return (value - low) / (high - low)


def medical_diagnosis():
    print("\n--- Medical Diagnosis ---")
    temperature = 38
    fever = fuzzy_membership(temperature, 36, 40)

    risk = "High" if fever > 0.5 else "Low"
    print(f"Body temperature: {temperature} C")
    print(f"Fever membership: {fever:.2f}")
    print(f"Illustrative risk level: {risk}")


def electric_vehicle():
    print("\n--- Electric Vehicle ---")
    battery_temperature = 45
    risk = fuzzy_membership(battery_temperature, 30, 60)

    action = "Warning" if risk > 0.5 else "Normal"
    print(f"Battery temperature: {battery_temperature} C")
    print(f"Battery risk membership: {risk:.2f}")
    print(f"Action: {action}")


def autonomous_vehicle():
    print("\n--- Autonomous Vehicle ---")
    obstacle_distance = 15

    braking_membership = 1 - fuzzy_membership(
        obstacle_distance, 5, 50
    )
    braking_intensity = braking_membership * 100

    print(f"Obstacle distance: {obstacle_distance} m")
    print(f"Braking intensity: {braking_intensity:.2f}%")


def smart_manufacturing():
    print("\n--- Smart Manufacturing ---")
    machine_temperature = 85
    risk = fuzzy_membership(machine_temperature, 50, 100)

    maintenance = "Required" if risk > 0.7 else "Not required"
    print(f"Machine temperature: {machine_temperature} C")
    print(f"Machine risk membership: {risk:.2f}")
    print(f"Maintenance: {maintenance}")


def main():
    while True:
        print("\n===== FUZZY INFERENCING SYSTEM =====")
        print("1. Medical Diagnosis")
        print("2. Electric Vehicle")
        print("3. Autonomous Vehicle")
        print("4. Smart Manufacturing")
        print("5. Run All Use Cases")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            medical_diagnosis()
        elif choice == "2":
            electric_vehicle()
        elif choice == "3":
            autonomous_vehicle()
        elif choice == "4":
            smart_manufacturing()
        elif choice == "5":
            medical_diagnosis()
            electric_vehicle()
            autonomous_vehicle()
            smart_manufacturing()
        elif choice == "0":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
