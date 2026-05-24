def generate_explanation(
    percentages
):

    visual = percentages["visual"]

    auditory = percentages["auditory"]

    kinesthetic = percentages["kinesthetic"]

    dominant = max(
        percentages,
        key=percentages.get
    )

    sorted_scores = sorted(

        percentages.items(),

        key=lambda x: x[1],

        reverse=True

    )

    secondary = sorted_scores[1][0]
    sorted_scores[1][0]

    difference = (
        sorted_scores[0][1]
        -
        sorted_scores[1][1]
    )

    primary_score = sorted_scores[0][1]

    secondary_score = sorted_scores[1][1]

    # MULTIMODAL

        # BALANCED STYLE

    if difference <= 5:

        return f"""

        Anda memiliki keseimbangan
        gaya belajar
        {dominant} dan {secondary}.

        Anda mampu memahami materi
        dengan baik melalui lebih
        dari satu pendekatan belajar.

        Kombinasi ini menunjukkan
        fleksibilitas belajar yang baik
        dan kemampuan adaptasi
        terhadap berbagai metode pembelajaran.

        """

    # SECONDARY TENDENCY

    elif difference <= 15:

        return f"""

        Anda memiliki kecenderungan
        gaya belajar {dominant}
        dengan dukungan gaya belajar
        {secondary} yang cukup kuat.

        Anda cenderung lebih nyaman
        belajar menggunakan metode
        {dominant}, namun metode
        {secondary} juga membantu
        proses pemahaman materi Anda.

        """