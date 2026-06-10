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

    goals = {

        "visual": visual,

        "auditory": auditory,

        "kinesthetic": kinesthetic

    }

    dominant = max(

        goals,

        key=goals.get

    )

    explanation = f"""

Sistem memulai proses inferensi
dari tiga hipotesis gaya belajar:

1. Visual
2. Auditori
3. Kinestetik

Fakta yang diperoleh dari hasil
jawaban pengguna adalah:

Visual      : {visual} jawaban

Auditori    : {auditory} jawaban

Kinestetik  : {kinesthetic} jawaban

Sistem kemudian membandingkan
jumlah fakta yang mendukung
masing-masing hipotesis.

Hipotesis dengan jumlah fakta
terbanyak diterima sebagai
kesimpulan akhir.

Hasil inferensi menunjukkan bahwa
gaya belajar {dominant.capitalize()}
memiliki fakta pendukung paling banyak.

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
        explanation

    }