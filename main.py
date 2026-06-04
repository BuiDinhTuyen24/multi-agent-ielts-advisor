import pandas as pd

from crewai import Crew

from agents import (
    student_analyzer,
    learning_advisor,
    feedback_agent
)

from tasks import create_tasks


def run_student(student):

    tasks = create_tasks(
        student,
        student_analyzer,
        learning_advisor,
        feedback_agent
    )

    crew = Crew(
        agents=[
            student_analyzer,
            learning_advisor,
            feedback_agent
        ],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result


def main():

    df = pd.read_csv("students.csv")

    print("\nDanh sách học viên:")
    print("-" * 50)

    for idx, row in df.iterrows():
        print(f"{idx + 1}. {row['name']}")

    print("-" * 50)

    choice = int(input("Chọn học viên (số thứ tự): "))

    student = df.iloc[choice - 1].to_dict()

    print(f"\nProcessing: {student['name']}")
    print("=" * 50)

    report = run_student(student)

    with open(
        f"output/{student['name']}_report.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(str(report))

    print(
        f"\nReport saved to output/{student['name']}_report.txt"
    )


if __name__ == "__main__":
    main()