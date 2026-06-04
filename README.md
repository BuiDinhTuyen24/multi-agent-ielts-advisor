# Agentic IELTS Learning System

An AI-powered Learning Management System (LMS) demo built with CrewAI and Gemini.

This project uses multiple AI agents to analyze IELTS student performance, identify weak skills, and generate personalized learning recommendations based on current scores and target band goals.

---

## Features

* Analyze IELTS student data from CSV files
* Evaluate Listening, Reading, Writing, and Speaking scores
* Compare current performance against target overall band
* Identify strengths and weaknesses
* Generate personalized study plans
* Produce automated feedback reports
* Demonstrate a Multi-Agent AI workflow using CrewAI

---

## System Architecture

### Agent 1 — Student Analyzer

Responsibilities:

* Analyze student IELTS scores
* Calculate current performance level
* Identify weak and strong skills
* Summarize learning needs

### Agent 2 — Learning Advisor

Responsibilities:

* Generate a personalized study plan
* Recommend learning priorities
* Suggest improvement strategies
* Estimate progress path toward target band

### Agent 3 — Feedback Agent

Responsibilities:

* Review recommendations
* Improve clarity and usefulness
* Produce final student report

---

## Project Structure

```text
agentic-ielts-learning-system/
│
├── agents.py
├── tasks.py
├── main.py
├── students.csv
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
└── output/
    └── reports.txt
```

---

## Example Student Data

```csv
student_id,name,listening,reading,writing,speaking,target_band
1001,Nguyen Van A,5.5,5.0,4.5,5.0,6.5
1002,Tran Thi B,6.0,6.5,5.5,5.5,7.0
1003,Le Van C,4.5,4.0,4.5,5.0,6.0
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/agentic-ielts-learning-system.git
cd agentic-ielts-learning-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Example template:

```env
GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxx
```

---

## Run the Project

```bash
python main.py
```

The system will:

1. Load student data from `students.csv`
2. Select a student
3. Run the multi-agent workflow
4. Generate a personalized IELTS report
5. Save results to the `output` folder

---

## Example Output

```text
Student: Nguyen Van A

Current Scores:
Listening: 5.5
Reading: 5.0
Writing: 4.5
Speaking: 5.0

Target Overall Band: 6.5

Weakest Skill:
Writing

Recommended Learning Plan:
- Focus on Task 2 essay structure
- Practice grammar accuracy daily
- Write 3 essays per week
- Review high-band sample answers

Estimated Improvement Timeline:
3-4 months of consistent study
```

---

## Technologies Used

* Python
* CrewAI
* Google Gemini 2.5 Flash
* Pandas
* dotenv

---

## Educational Purpose

This project was developed as a demonstration of Multi-Agent AI systems in an educational LMS scenario.

It showcases how AI agents can collaborate to analyze learner data and generate personalized recommendations automatically.

---

## Future Improvements

* Web interface with Streamlit
* Student database integration
* Progress tracking dashboard
* Historical score analysis
* CRM integration for student management
* Email-based study recommendations

---

## Author

Bui Dinh Tuyen

Data Science / AI Student
