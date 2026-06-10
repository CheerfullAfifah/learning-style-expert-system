import random

questions = [

    {
        "id": "q1",
        "question": "Ketika guru menjelaskan materi baru, hal yang paling membantumu memahami pelajaran adalah...",
        "options": [
            {"text": "melihat gambar, diagram, atau video", "type": "visual"},
            {"text": "mendengarkan penjelasan guru", "type": "auditory"},
            {"text": "mencoba langsung melalui praktik", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q2",
        "question": "Saat belajar di rumah, kamu biasanya lebih nyaman dengan cara...",
        "options": [
            {"text": "membuat catatan berwarna atau mind map", "type": "visual"},
            {"text": "mengulang materi dengan suara", "type": "auditory"},
            {"text": "belajar sambil bergerak", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q3",
        "question": "Ketika menghafal pelajaran, kamu lebih mudah mengingat...",
        "options": [
            {"text": "bentuk tulisan, warna, atau gambar", "type": "visual"},
            {"text": "suara atau penjelasan yang didengar", "type": "auditory"},
            {"text": "hal yang pernah dipraktikkan", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q4",
        "question": "Saat guru memberikan tugas kelompok, kamu lebih tertarik untuk...",
        "options": [
            {"text": "membuat desain atau slide presentasi", "type": "visual"},
            {"text": "menjelaskan materi kepada kelompok", "type": "auditory"},
            {"text": "menyiapkan demonstrasi atau praktik", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q5",
        "question": "Saat mempelajari hal baru, kamu biasanya lebih suka...",
        "options": [
            {"text": "melihat contoh visual terlebih dahulu", "type": "visual"},
            {"text": "mendengar penjelasan terlebih dahulu", "type": "auditory"},
            {"text": "langsung mencoba sendiri", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q6",
        "question": "Ketika belajar di kelas, kamu paling fokus jika...",
        "options": [
            {"text": "guru menggunakan gambar atau video", "type": "visual"},
            {"text": "guru menjelaskan dengan menarik", "type": "auditory"},
            {"text": "ada aktivitas praktik", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q7",
        "question": "Saat membaca buku pelajaran, kamu lebih suka jika...",
        "options": [
            {"text": "banyak gambar dan warna menarik", "type": "visual"},
            {"text": "dibaca sambil bersuara pelan", "type": "auditory"},
            {"text": "disertai aktivitas praktik", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q8",
        "question": "Ketika suasana kelas ramai, kamu biasanya tetap bisa belajar jika...",
        "options": [
            {"text": "masih bisa melihat materi dengan jelas", "type": "visual"},
            {"text": "masih bisa mendengar penjelasan", "type": "auditory"},
            {"text": "tetap melakukan aktivitas belajar", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q9",
        "question": "Saat menggunakan HP untuk belajar, kamu paling sering...",
        "options": [
            {"text": "menonton video pembelajaran", "type": "visual"},
            {"text": "mendengarkan podcast atau audio", "type": "auditory"},
            {"text": "mengikuti simulasi interaktif", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q10",
        "question": "Jika guru memberi instruksi, kamu lebih cepat memahami ketika...",
        "options": [
            {"text": "instruksi ditulis atau diperlihatkan", "type": "visual"},
            {"text": "instruksi dijelaskan langsung", "type": "auditory"},
            {"text": "instruksi dicontohkan langsung", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q11",
        "question": "Saat belajar bersama teman, kamu lebih nyaman jika...",
        "options": [
            {"text": "ada catatan atau gambar yang bisa dilihat bersama", "type": "visual"},
            {"text": "belajar sambil berdiskusi", "type": "auditory"},
            {"text": "belajar sambil praktik", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q12",
        "question": "Hal yang paling mudah kamu ingat setelah belajar biasanya adalah...",
        "options": [
            {"text": "apa yang kamu lihat", "type": "visual"},
            {"text": "apa yang kamu dengar", "type": "auditory"},
            {"text": "apa yang kamu lakukan", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q13",
        "question": "Ketika guru menjelaskan terlalu lama, kamu biasanya...",
        "options": [
            {"text": "mulai mencoret-coret catatan", "type": "visual"},
            {"text": "masih mendengarkan penjelasan", "type": "auditory"},
            {"text": "mulai ingin bergerak", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q14",
        "question": "Saat diminta menjelaskan sesuatu kepada teman, kamu lebih sering...",
        "options": [
            {"text": "menggunakan gambar atau tulisan", "type": "visual"},
            {"text": "menjelaskan dengan berbicara", "type": "auditory"},
            {"text": "mencontohkan secara langsung", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q15",
        "question": "Ketika melihat informasi baru, perhatianmu biasanya tertuju pada...",
        "options": [
            {"text": "warna, bentuk, atau tampilan visual", "type": "visual"},
            {"text": "cara penyampaian penjelasan", "type": "auditory"},
            {"text": "aktivitas yang bisa dilakukan", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q16",
        "question": "Saat sedang santai, aktivitas yang paling kamu sukai adalah...",
        "options": [
            {"text": "menonton video atau melihat gambar", "type": "visual"},
            {"text": "mendengarkan musik atau ngobrol", "type": "auditory"},
            {"text": "melakukan aktivitas fisik", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q17",
        "question": "Jika ada alat peraga di kelas, kamu biasanya lebih suka...",
        "options": [
            {"text": "memperhatikan bentuk dan tampilannya", "type": "visual"},
            {"text": "mendengarkan penjelasannya", "type": "auditory"},
            {"text": "mencobanya secara langsung", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q18",
        "question": "Saat mengerjakan tugas sulit, kamu biasanya...",
        "options": [
            {"text": "mencari contoh visual", "type": "visual"},
            {"text": "bertanya atau berdiskusi", "type": "auditory"},
            {"text": "mencoba sendiri berkali-kali", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q19",
        "question": "Saat mengikuti pembelajaran online, kamu lebih nyaman jika...",
        "options": [
            {"text": "materinya penuh visual dan animasi", "type": "visual"},
            {"text": "penjelasan suara terdengar jelas", "type": "auditory"},
            {"text": "ada tugas praktik atau interaksi", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q20",
        "question": "Saat bermain game edukasi, bagian yang paling kamu sukai adalah...",
        "options": [
            {"text": "tampilan visual game", "type": "visual"},
            {"text": "suara dan dialog game", "type": "auditory"},
            {"text": "gerakan dan aksi dalam game", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q21",
        "question": "Kegiatan sekolah yang paling membuatmu semangat biasanya adalah...",
        "options": [
            {"text": "yang memiliki tampilan menarik", "type": "visual"},
            {"text": "yang banyak diskusi dan komunikasi", "type": "auditory"},
            {"text": "yang melibatkan praktik langsung", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q22",
        "question": "Saat mempelajari materi baru, kamu lebih mudah memahami jika...",
        "options": [
            {"text": "ada diagram atau ilustrasi", "type": "visual"},
            {"text": "ada penjelasan verbal yang jelas", "type": "auditory"},
            {"text": "ada percobaan atau simulasi", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q23",
        "question": "Ketika belajar untuk ujian, kamu lebih sering...",
        "options": [
            {"text": "membaca ulang catatan atau rangkuman", "type": "visual"},
            {"text": "mengulang materi dengan suara", "type": "auditory"},
            {"text": "belajar sambil bergerak", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q24",
        "question": "Jika diminta membuat suatu karya, kamu lebih suka...",
        "options": [
            {"text": "mendesain tampilan yang menarik", "type": "visual"},
            {"text": "menjelaskan ide kepada orang lain", "type": "auditory"},
            {"text": "membuat model atau praktik langsung", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q25",
        "question": "Saat belajar kelompok, kamu paling sering...",
        "options": [
            {"text": "menulis atau membuat rangkuman visual", "type": "visual"},
            {"text": "berdiskusi dan bertukar pendapat", "type": "auditory"},
            {"text": "menyiapkan aktivitas praktik", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q26",
        "question": "Saat guru memberikan contoh materi, kamu lebih mudah memahami jika...",
        "options": [
            {"text": "contohnya berupa gambar atau ilustrasi", "type": "visual"},
            {"text": "contohnya dijelaskan secara lisan", "type": "auditory"},
            {"text": "contohnya dipraktikkan langsung", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q27",
        "question": "Ketika belajar sesuatu yang baru, langkah pertama yang biasanya kamu lakukan adalah...",
        "options": [
            {"text": "melihat contoh atau tampilan visual", "type": "visual"},
            {"text": "mendengarkan penjelasan terlebih dahulu", "type": "auditory"},
            {"text": "langsung mencoba sendiri", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q28",
        "question": "Saat suasana kelas mulai membosankan, kamu biasanya...",
        "options": [
            {"text": "melihat-lihat catatan atau gambar", "type": "visual"},
            {"text": "mengobrol dengan teman", "type": "auditory"},
            {"text": "bergerak atau memainkan sesuatu", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q29",
        "question": "Saat mengikuti presentasi di kelas, bagian yang paling membantumu memahami materi adalah...",
        "options": [
            {"text": "slide dan visual presentasi", "type": "visual"},
            {"text": "cara pembicara menjelaskan", "type": "auditory"},
            {"text": "demonstrasi atau simulasi langsung", "type": "kinesthetic"}
        ]
    },

    {
        "id": "q30",
        "question": "Menurutmu, cara belajar yang paling menyenangkan adalah...",
        "options": [
            {"text": "belajar dengan tampilan visual menarik", "type": "visual"},
            {"text": "belajar sambil berdiskusi", "type": "auditory"},
            {"text": "belajar sambil praktik langsung", "type": "kinesthetic"}
        ]
    }

]

for q in questions:
    random.shuffle(q["options"])