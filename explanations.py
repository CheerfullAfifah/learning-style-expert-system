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

    difference = (
        sorted_scores[0][1]
        -
        sorted_scores[1][1]
    )

    # MULTIMODAL

    if difference <= 10:

        return f"""

        Anda memiliki kombinasi
        gaya belajar
        {dominant} dan {secondary}.

        Anda cenderung dapat
        memahami materi melalui
        lebih dari satu metode belajar.

        Kombinasi ini menunjukkan
        kemampuan adaptasi belajar
        yang cukup baik.

        """

    # VISUAL

    if dominant == "visual":

        return """

        Anda memiliki kecenderungan
        gaya belajar visual.

        Anda lebih mudah memahami
        materi melalui gambar,
        warna, diagram,
        video, dan tampilan visual.

        Membuat mind mapping,
        catatan berwarna,
        dan melihat ilustrasi
        dapat membantu proses belajar Anda.

        """

    # AUDITORY

    elif dominant == "auditory":

        return """

        Anda memiliki kecenderungan
        gaya belajar auditory.

        Anda lebih mudah memahami
        materi melalui penjelasan verbal,
        diskusi, dan mendengarkan.

        Belajar sambil berdiskusi,
        mendengarkan penjelasan,
        atau mengulang materi dengan suara
        dapat membantu Anda memahami pelajaran.

        """

    # KINESTHETIC

    else:

        return """

        Anda memiliki kecenderungan
        gaya belajar kinesthetic.

        Anda lebih mudah memahami
        materi melalui praktik langsung,
        simulasi, dan aktivitas fisik.

        Belajar sambil mencoba,
        praktik, dan melakukan aktivitas
        dapat membantu Anda memahami materi.

        """