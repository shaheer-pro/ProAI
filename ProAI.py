import json
from difflib import get_close_matches

def load_knoledge(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)

    return data

def save_knoledge(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def find_best_match(user_questions: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_questions, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_awnser_for_questions(question: str, knoledge: dict) -> str | None:
    for q in knoledge["questions"]:
        if q["questions"] == question:
            return q["awnser"]

def chat_bot():
    knoledge: dict = load_knoledge("knoledge.json")

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == "quit":
            break

        best_match: str | None = find_best_match(user_input, [q["questions"] for q in knoledge["questions"]]) 
        
        if best_match:
            awnser: str = get_awnser_for_questions(best_match, knoledge)
            print(f"ProAI: {awnser}")
        else:
            print("ProAI: I dont know the awnser. Kindly Teach Me.")
            new_awnser: str = input("Type the awnser or 'skip to skip: ")    
            if new_awnser.lower() != "skip":
                knoledge["questions"].append({"questions": user_input, "awnser": new_awnser})
                save_knoledge("knoledge.json", knoledge)
                print("Bot: Thank you so much! I learned somthing new!!!")

if __name__ == "__main__":
    chat_bot()

