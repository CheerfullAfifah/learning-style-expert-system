# =====================================
# RESULT CALCULATION
# =====================================

def calculate_result(

    questions,
    answers

):

    scores = {

        "visual": 0,

        "auditory": 0,

        "kinesthetic": 0

    }

    for q in questions:

        question_id = str(
            q["id"]
        )

        selected_answer = answers.get(
            question_id
        )

        if selected_answer in scores:

            scores[
                selected_answer
            ] += 1

    total = sum(
        scores.values()
    )

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

            for key, value
            in scores.items()

        }

    dominant = max(

        scores,

        key=scores.get

    )

    return dominant, percentages, scores


# =====================================
# BACKWARD CHAINING
# =====================================

def backward_chaining(

    scores

):

    visual = scores[
        "visual"
    ]

    auditory = scores[
        "auditory"
    ]

    kinesthetic = scores[
        "kinesthetic"
    ]

    # =====================================
    # GOAL : VISUAL
    # =====================================

    if (
        visual >= auditory
        and
        visual >= kinesthetic
    ):

        dominant = "visual"

        rule_trace = f"""

GOAL:
Visual Dominan

RULE:
Visual >= Auditori
AND
Visual >= Kinestetik

FAKTA:
Visual      = {visual}
Auditori    = {auditory}
Kinestetik  = {kinesthetic}

HASIL:
Rule terpenuhi

KESIMPULAN:
Visual merupakan gaya belajar dominan.

"""

    # =====================================
    # GOAL : AUDITORY
    # =====================================

    elif (
        auditory >= visual
        and
        auditory >= kinesthetic
    ):

        dominant = "auditory"

        rule_trace = f"""

GOAL:
Auditori Dominan

RULE:
Auditori >= Visual
AND
Auditori >= Kinestetik

FAKTA:
Visual      = {visual}
Auditori    = {auditory}
Kinestetik  = {kinesthetic}

HASIL:
Rule terpenuhi

KESIMPULAN:
Auditori merupakan gaya belajar dominan.

"""

    # =====================================
    # GOAL : KINESTHETIC
    # =====================================

    else:

        dominant = "kinesthetic"

        rule_trace = f"""

GOAL:
Kinestetik Dominan

RULE:
Kinestetik >= Visual
AND
Kinestetik >= Auditori

FAKTA:
Visual      = {visual}
Auditori    = {auditory}
Kinestetik  = {kinesthetic}

HASIL:
Rule terpenuhi

KESIMPULAN:
Kinestetik merupakan gaya belajar dominan.

"""

    return {

        "goal": dominant,

        "visual_count":
        visual,

        "auditory_count":
        auditory,

        "kinesthetic_count":
        kinesthetic,

        "rule_trace":
        rule_trace

    }