let questions = [];
let index = 0;
let score = 0;

fetch('/questions')
    .then(res => res.json())
    .then(data => {
        questions = data;
        showQuestion();
    });

function showQuestion() {
    let q = questions[index];
    document.getElementById("question").innerText = q.question;

    let answersDiv = document.getElementById("answers");
    answersDiv.innerHTML = "";

    q.choices.forEach(choice => {
        let btn = document.createElement("button");
        btn.innerText = choice;

        btn.onclick = () => {
            if (choice === q.answer) {
                score++;
                showToast("✅ Correct !", "correct");
            } else {
                showToast("❌ Faux !", "wrong");
            }

            index++;

            if (index < questions.length) {
                showQuestion();
            } else {
                showResult();
            }
        };

        answersDiv.appendChild(btn);
    });
}

function showResult() {
    document.getElementById("quiz").innerHTML =
        `<h2>Score final : ${score}/${questions.length}</h2>`;
}
function showToast(message, type) {
    let toast = document.getElementById("toast");

    toast.innerText = message;
    toast.className = "show " + type;

    setTimeout(() => {
        toast.className = toast.className.replace("show", "");
    }, 1500); // disparaît après 1.5 sec
}