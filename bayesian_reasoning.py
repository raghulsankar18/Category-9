def bayes_theorem(prior, likelihood, evidence):
    """Calculate posterior probability using Bayes' theorem."""
    if evidence <= 0:
        raise ValueError("Evidence probability must be greater than zero.")

    for probability in (prior, likelihood, evidence):
        if not 0 <= probability <= 1:
            raise ValueError("All probabilities must be between 0 and 1.")

    return (prior * likelihood) / evidence


def medical_diagnosis():
    print("\n--- Medical Diagnosis ---")
    prior = 0.10
    likelihood = 0.80
    evidence = 0.20

    posterior = bayes_theorem(prior, likelihood, evidence)
    print(f"Probability of disease: {posterior * 100:.2f}%")


def electric_vehicle():
    print("\n--- Electric Vehicle ---")
    prior = 0.15
    likelihood = 0.85
    evidence = 0.30

    posterior = bayes_theorem(prior, likelihood, evidence)
    print(f"Battery fault probability: {posterior * 100:.2f}%")


def autonomous_vehicle():
    print("\n--- Autonomous Vehicle ---")
    prior = 0.20
    likelihood = 0.90
    evidence = 0.40

    posterior = bayes_theorem(prior, likelihood, evidence)
    print(f"Collision risk probability: {posterior * 100:.2f}%")


def smart_manufacturing():
    print("\n--- Smart Manufacturing ---")
    prior = 0.12
    likelihood = 0.75
    evidence = 0.25

    posterior = bayes_theorem(prior, likelihood, evidence)
    print(f"Machine failure probability: {posterior * 100:.2f}%")


def main():
    while True:
        print("\n===== BAYESIAN REASONING =====")
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
