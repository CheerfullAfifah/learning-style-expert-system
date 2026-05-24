def calculate_result(questions, answers):

    scores = {

        "visual": 0,

        "auditory": 0,

        "kinesthetic": 0

    }

    for q in questions:

        question_id = q["id"]

        selected_answer = answers.get(question_id)

        if selected_answer in scores:

            scores[selected_answer] += 1

    total = sum(scores.values())

    if total == 0:

        percentages = {

            "visual": 0,

            "auditory": 0,

            "kinesthetic": 0

        }

    else:

        percentages = {

            key: round(
                (value / total) * 100,
                2
            )

            for key, value in scores.items()

        }

    dominant = max(
        scores,
        key=scores.get
    )

    return dominant, percentages