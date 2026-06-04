from crewai import Agent, LLM

llm = LLM(
    model="gemini/gemini-2.5-flash"
)

student_analyzer = Agent(
    role="Student Analyzer",
    goal="Analyze IELTS student performance and identify strengths and weaknesses",
    backstory="""
    You are an experienced IELTS academic manager.
    You analyze student performance and determine learning priorities.
    """,
    llm=llm,
    verbose=True
)

learning_advisor = Agent(
    role="Learning Advisor",
    goal="Create personalized IELTS study plans",
    backstory="""
    You are an IELTS curriculum specialist.
    You create detailed study plans based on student weaknesses.
    """,
    llm=llm,
    verbose=True
)

feedback_agent = Agent(
    role="Feedback Agent",
    goal="Generate final IELTS reports and recommendations",
    backstory="""
    You are a senior IELTS consultant.
    You provide professional feedback and predictions.
    """,
    llm=llm,
    verbose=True
)