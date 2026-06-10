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

        if style == "visual":
            return "Visual"

        elif style == "auditory":
            return "Auditori"

        return "Kinestetik"

    primary_text = translate(primary)

    secondary_text = translate(secondary)

    tertiary_text = translate(tertiary)

    explanation = f"""

    Gaya belajar dominan Anda adalah
    {primary_text} ({primary_score}%).

    """

    # =====================================
    # PRIMARY DESCRIPTION
    # =====================================

    if primary == "visual":

        explanation += """

        Anda cenderung lebih mudah memahami
        materi melalui gambar, video,
        warna, diagram, dan visualisasi.

        """

    elif primary == "auditory":

        explanation += """

        Anda cenderung lebih mudah memahami
        materi melalui penjelasan verbal,
        diskusi, dan aktivitas mendengarkan.

        """

    else:

        explanation += """

        Anda cenderung lebih mudah memahami
        materi melalui praktik langsung,
        aktivitas, dan pengalaman nyata.

        """

    # =====================================
    # SECONDARY STYLE
    # =====================================

    explanation += f"""

    Gaya belajar kedua Anda adalah
    {secondary_text} ({secondary_score}%).

    """

    if secondary == "visual":

        explanation += """

        Hal ini menunjukkan bahwa pendekatan
        visual juga membantu memperkuat
        pemahaman materi Anda.

        """

    elif secondary == "auditory":

        explanation += """

        Hal ini menunjukkan bahwa penjelasan verbal
        dan diskusi juga membantu proses belajar Anda.

        """

    else:

        explanation += """

        Hal ini menunjukkan bahwa praktik langsung
        dan aktivitas juga membantu memperkuat
        pemahaman Anda.

        """

    # =====================================
    # TERTIARY STYLE
    # =====================================

    explanation += f"""

    Sementara itu, gaya belajar
    {tertiary_text} ({tertiary_score}%)
    tetap berperan sebagai pendukung
    dalam proses belajar Anda.

    """

    return explanation