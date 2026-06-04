from crewai import Task


def create_tasks(student, analyzer, advisor, feedback):

    analyze_task = Task(
        description=f"""
        Analyze the following IELTS student.

        Student Data:
        {student}

        Calculate:
        1. Current overall band score
        2. Weakest skill
        3. Strongest skill
        4. Gap to target overall score
        5. Main learning priority

        Provide detailed analysis.
        """,
        agent=analyzer,
        expected_output="""
        Detailed student analysis including:
        overall score,
        weakest skill,
        strongest skill,
        gap to target,
        learning priorities.
        """
    )

    study_plan_task = Task(
        description="""
        Create a personalized IELTS study plan.

        Use the analysis results.

        Requirements:
        - Weekly study allocation
        - Skill priorities
        - Recommended activities
        - Estimated improvement timeline
        """,
        agent=advisor,
        context=[analyze_task],
        expected_output="""
        Detailed weekly study plan with time allocation.
        """
    )

    final_report_task = Task(
        description="""
        Generate a final professional IELTS report.

        Include:
        - Student summary
        - Current level
        - Target score
        - Weaknesses
        - Study plan
        - Estimated timeline
        - Final recommendations
        """,
        agent=feedback,
        context=[analyze_task, study_plan_task],
        expected_output="""
        Complete IELTS student report.
        """
    )

    return [analyze_task, study_plan_task, final_report_task]