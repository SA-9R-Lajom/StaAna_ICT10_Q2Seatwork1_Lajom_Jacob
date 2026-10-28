from pyscript import document 

club_members = [
    "Jake Santos",
    "Mark Reyes",
    "John Cruz",
    "Daniel Garcia",
    "Michael Torres",
    "Joshua Mendoza",
    "Adrian Flores",
    "Nathan Ramos",
    "Gabriel Castillo",
    "Ethan Navarro"
]


def verify_candidate(event):

    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()

    full_name = first_name.title() + " " + last_name.title()

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the Car Enthusiast Club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    result = document.getElementById("result")

    result.innerText = messages[is_member]

    result.classList.remove("d-none")

    result.classList.remove("text-success", "text-danger")

    result.classList.add(
        {True: "text-success", False: "text-danger"}[is_member]
    )

    result.style.backgroundColor = {
        True: "#173b27",
        False: "#451d1d" 
        }
    [is_member]
