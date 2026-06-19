def generate_explanation(percentages):

    sorted_scores = sorted(
        percentages.items(),
        key=lambda x: x[1],
        reverse=True
    )

    primary = sorted_scores[0][0]

    def translate(style):

        if style == "visual":
            return "Visual"

        elif style == "auditory":
            return "Auditori"

        return "Kinestetik"

    if primary == "visual":

        return (
            "Anda cenderung lebih mudah memahami materi "
            "melalui gambar, video, warna, diagram, "
            "dan visualisasi."
        )

    elif primary == "auditory":

        return (
            "Anda cenderung lebih mudah memahami materi "
            "melalui penjelasan verbal, diskusi, "
            "dan aktivitas mendengarkan."
        )

    return (
        "Anda cenderung lebih mudah memahami materi "
        "melalui praktik langsung, aktivitas, "
        "dan pengalaman nyata."
    )


def generate_analysis_extra(percentages):

    sorted_scores = sorted(
        percentages.items(),
        key=lambda x: x[1],
        reverse=True
    )

    primary = sorted_scores[0]
    secondary = sorted_scores[1]
    tertiary = sorted_scores[2]

    def translate(style):

        if style == "visual":
            return "Visual"

        elif style == "auditory":
            return "Auditori"

        return "Kinestetik"

    primary_name = translate(primary[0])
    secondary_name = translate(secondary[0])
    tertiary_name = translate(tertiary[0])

    return (
        f"Berdasarkan hasil kuis, gaya belajar dominan kamu adalah "
        f"{primary_name} ({primary[1]}%). "
        f"Hal ini menunjukkan bahwa metode belajar yang paling efektif "
        f"adalah yang menyesuaikan karakteristik {primary_name.lower()}.\n\n"

        f"Gaya belajar kedua adalah "
        f"{secondary_name} ({secondary[1]}%), "
        f"yang juga berperan dalam membantu proses pemahaman materi.\n\n"

        f"Sementara itu, gaya belajar "
        f"{tertiary_name} ({tertiary[1]}%) "
        f"tetap menjadi pendukung sehingga kombinasi ketiga gaya belajar "
        f"tetap dapat digunakan secara seimbang sesuai situasi belajar."
    )