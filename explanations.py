def generate_explanation(
    percentages
):

    sorted_scores = sorted(

        percentages.items(),

        key=lambda x: x[1],

        reverse=True

    )

    primary = sorted_scores[0][0]
    primary_score = sorted_scores[0][1]

    secondary = sorted_scores[1][0]
    secondary_score = sorted_scores[1][1]

    tertiary = sorted_scores[2][0]
    tertiary_score = sorted_scores[2][1]

    def translate(style):

        mapping = {

            "visual": "Visual",

            "auditory": "Auditori",

            "kinesthetic": "Kinestetik"

        }

        return mapping[style]

    primary_text = translate(primary)

    secondary_text = translate(secondary)

    tertiary_text = translate(tertiary)

    # =====================================
    # RINGKASAN DOMINAN
    # =====================================

    if primary == "visual":

        summary = (
            "Lebih efektif memahami informasi melalui "
            "gambar, diagram, warna, dan visualisasi."
        )

    elif primary == "auditory":

        summary = (
            "Lebih efektif memahami materi melalui "
            "diskusi, penjelasan verbal, dan media audio."
        )

    else:

        summary = (
            "Lebih efektif belajar melalui praktik, "
            "simulasi, dan pengalaman langsung."
        )

    return {

        "primary": primary_text,

        "primary_score": primary_score,

        "secondary": secondary_text,

        "secondary_score": secondary_score,

        "tertiary": tertiary_text,

        "tertiary_score": tertiary_score,

        "summary": summary

    }