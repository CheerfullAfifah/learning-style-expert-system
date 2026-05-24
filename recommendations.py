recommendations = {

    "visual": {

        "student": [

            "Gunakan mind mapping saat belajar",

            "Gunakan warna pada catatan",

            "Belajar menggunakan video pembelajaran",

            "Gunakan diagram atau gambar",

            "Buat rangkuman visual"

        ],

        "teacher": [

            "Gunakan media gambar saat mengajar",

            "Gunakan slide yang menarik",

            "Gunakan diagram dan ilustrasi",

            "Tuliskan poin penting di papan",

            "Berikan video pembelajaran"

        ],

        "parent": [

            "Bantu anak belajar menggunakan video",

            "Gunakan catatan berwarna",

            "Berikan buku bergambar",

            "Ajak anak membuat mind map",

            "Gunakan media visual saat belajar di rumah"

        ]

    },

    "auditory": {

        "student": [

            "Belajar dengan diskusi",

            "Gunakan rekaman suara",

            "Belajar sambil berbicara",

            "Dengarkan penjelasan materi",

            "Belajar bersama teman"

        ],

        "teacher": [

            "Gunakan penjelasan verbal",

            "Ajak siswa berdiskusi",

            "Gunakan presentasi lisan",

            "Berikan kesempatan bertanya",

            "Gunakan metode tanya jawab"

        ],

        "parent": [

            "Ajak anak berdiskusi",

            "Dengarkan anak menjelaskan pelajaran",

            "Gunakan audio pembelajaran",

            "Bacakan materi bersama",

            "Dukung anak belajar kelompok"

        ]

    },

    "kinesthetic": {

        "student": [

            "Belajar dengan praktik langsung",

            "Gunakan simulasi",

            "Belajar sambil bergerak",

            "Lakukan eksperimen sederhana",

            "Gunakan permainan edukatif"

        ],

        "teacher": [

            "Gunakan metode praktik",

            "Kurangi ceramah terlalu lama",

            "Gunakan aktivitas kelas",

            "Berikan simulasi",

            "Gunakan pembelajaran interaktif"

        ],

        "parent": [

            "Ajak anak belajar sambil praktik",

            "Gunakan aktivitas langsung",

            "Berikan eksperimen sederhana",

            "Jangan hanya fokus membaca",

            "Berikan media belajar interaktif"

        ]

    }

}

def get_recommendations(
    dominant,
    percentages
):

    visual = percentages["visual"]

    auditory = percentages["auditory"]

    kinesthetic = percentages["kinesthetic"]

    sorted_scores = sorted(

        percentages.items(),

        key=lambda x: x[1],

        reverse=True

    )

    primary = sorted_scores[0][0]

    secondary = sorted_scores[1][0]

    difference = (
        sorted_scores[0][1]
        -
        sorted_scores[1][1]
    )

    base = recommendations[dominant]

    student = base["student"][:]

    teacher = base["teacher"][:]

    parent = base["parent"][:]

    # =========================================
    # BALANCED LEARNING STYLE
    # =========================================

    if difference <= 5:

        student.append(
            f"Anda memiliki keseimbangan gaya belajar {primary} dan {secondary}. Gunakan kombinasi beberapa metode belajar agar pemahaman lebih optimal."
        )

        teacher.append(
            "Gunakan pendekatan pembelajaran yang bervariasi karena siswa mampu memahami materi melalui lebih dari satu metode belajar."
        )

        parent.append(
            "Berikan variasi metode belajar di rumah agar kemampuan belajar anak berkembang lebih optimal."
        )

    # =========================================
    # VISUAL + AUDITORY
    # =========================================

    elif (
        visual >= 35
        and
        auditory >= 25
    ):

        student.append(
            "Gunakan video pembelajaran, mind mapping, dan diskusi aktif untuk memperkuat pemahaman materi."
        )

        teacher.append(
            "Kombinasikan media visual dengan penjelasan verbal dan diskusi kelas."
        )

        parent.append(
            "Dukung anak belajar menggunakan video edukasi dan komunikasi aktif."
        )

    # =========================================
    # VISUAL + KINESTHETIC
    # =========================================

    elif (
        visual >= 35
        and
        kinesthetic >= 25
    ):

        student.append(
            "Gunakan media visual yang dipadukan dengan praktik langsung atau simulasi."
        )

        teacher.append(
            "Gunakan demonstrasi, eksperimen, dan project-based learning."
        )

        parent.append(
            "Berikan aktivitas belajar berbasis praktik dan visual di rumah."
        )

    # =========================================
    # AUDITORY + KINESTHETIC
    # =========================================

    elif (
        auditory >= 35
        and
        kinesthetic >= 25
    ):

        student.append(
            "Belajar melalui diskusi aktif, praktik langsung, dan simulasi kelompok."
        )

        teacher.append(
            "Gunakan pembelajaran interaktif berbasis aktivitas dan diskusi."
        )

        parent.append(
            "Ajak anak belajar sambil melakukan aktivitas sederhana dan komunikasi aktif."
        )

    # =========================================
    # HIGH VISUAL
    # =========================================

    if visual >= 60:

        student.append(
            "Kemampuan visual Anda sangat kuat. Gunakan diagram, warna, dan video untuk memaksimalkan pemahaman."
        )

    # =========================================
    # HIGH AUDITORY
    # =========================================

    if auditory >= 60:

        student.append(
            "Kemampuan auditori Anda sangat dominan. Diskusi, presentasi, dan penjelasan verbal akan sangat membantu proses belajar."
        )

    # =========================================
    # HIGH KINESTHETIC
    # =========================================

    if kinesthetic >= 60:

        student.append(
            "Kemampuan kinestetik Anda sangat dominan. Praktik langsung dan aktivitas fisik akan meningkatkan fokus belajar."
        )

    return {

        "student": student,

        "teacher": teacher,

        "parent": parent

    }