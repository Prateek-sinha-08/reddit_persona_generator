import os

def build_user_persona(username, analysis):
    file_path = f"output/{username}_persona.txt"
    os.makedirs("output", exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"USER PERSONA: u/{username}\n\n")

        f.write("---\n\n Motivations:\n")
        for item in analysis["citations"]:
            if "Motivations:" in item["analysis"]:
                f.write(f"{item['analysis'].split('Frustrations:')[0].strip()}\n\n")
                break

        f.write("---\n\n Frustrations:\n")
        for item in analysis["citations"]:
            if "Frustrations:" in item["analysis"]:
                f.write(f"{item['analysis'].split('Personality:')[0].split('Frustrations:')[-1].strip()}\n\n")
                break

        f.write("---\n\n Personality Traits:\n")
        for item in analysis["citations"]:
            if "Personality:" in item["analysis"]:
                f.write(f"{item['analysis'].split('Habits:')[0].split('Personality:')[-1].strip()}\n\n")
                break

        f.write("---\n\n Habits:\n")
        for item in analysis["citations"]:
            if "Habits:" in item["analysis"]:
                f.write(f"{item['analysis'].split('Goals:')[0].split('Habits:')[-1].strip()}\n\n")
                break

        f.write("---\n\n Goals & Needs:\n")
        for item in analysis["citations"]:
            if "Goals:" in item["analysis"]:
                f.write(f"{item['analysis'].split('Goals:')[-1].strip()}\n\n")
                break

        f.write("---\n\n Citations:\n")
        for item in analysis["citations"]:
            f.write(f"{item['url']}\n")
