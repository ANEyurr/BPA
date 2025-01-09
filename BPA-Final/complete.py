import random


# Global variables
name = ""
medical_supplies = random.randint(50, 100)
energy = random.randint(70, 100)
ewoks_treated = 0


def display_status():
    """
    Displays the medic's current status.
    """
    medical_supplies
    print(f"Hello, Medic, {name} Here is your inquiry.")
    print(f"your energy levels are {energy}. Your medical supplies are at {medical_supplies}. You have currently treated {ewoks_treated} Ewoks.")
    # TODO: Implement this function to print the medic's status
    # Hint: Include name, medical_supplies, energy, and ewoks_treated
pass


def treat_ewok():
    """
    Treats an Ewok based on random injury severity.
    Returns a message summarizing the treatment.
    """
    condition = random.choice("Minor", "Moderate", "Severe")
    if condition == "Minor":
        medical_supplies -= 10
        energy += 5
    elif condition == "Moderate":
        medical_supplies -= 20
    elif condition == "Severe":
        medical_supplies -= 30
        energy -= 10
    # TODO: Implement this function
    # 1. Randomly pick a condition: "Minor", "Moderate", or "Severe"
    # 2. Adjust medical_supplies and energy based on the condition
    # 3. Return a message about the treatment or lack of supplies
    # 4. Minor: -10 supplies, +5 energy.
    #    Moderate: -20 supplies, no energy change.
    #    Severe: -30 supplies, -10 energy.

    pass


def start_shift():
    """
    Starts the shift and runs encounters with Ewoks.
    """
    global name
    print("Welcome to the forest moon of Endor!")
    name = input("Enter your name, Medic: ")
    print(f"Welcome, Medic {name}. Ewoks are depending on you.")
    input("Press Enter when ready to begin your shift...")
   
    for _ in range(3):
        encounter_ewok()
        # TODO: Check if supplies or energy are 0 and break the loop if so
        # TODO: Call display_status to show the medic's progress
        pass
   
    # TODO: Call the end_shift function here
start_shift()

def encounter_ewok():
    """
    Simulates an encounter with an injured Ewok.
    """
    print("An injured Ewok needs your help!")
    while True:
        try:
            print(f"There is an injured Ewok near you! Act Fast!")
            task1 = input("Choose 1 to help an Ewok! To skip press 2.")
            if task1 == "1":
                print(f"You have chosen to help an Ewok, proceed with your supplies Medic.")
                treat_ewok()
            elif task1 == "2":
                print(f"You have chosen to skip this injury.")
            else:
                print(f"Value was incorrect choose either 1 or 2")
        except ValueError as e:
            print(e)
   
    # TODO: If the user chooses to treat the Ewok, call the treat_ewok function
    # TODO: If the user chooses to skip, return without treating
pass


def end_shift():
    """
    Ends the shift with a summary of the medic's performance.
    """
    # TODO: Implement this function
    # 1. Display a message based on remaining supplies and ewoks_treated
    # 2. Call display_status to show the final summary
    pass


# Start the shift
start_shift()
