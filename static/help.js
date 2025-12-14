let helpData = [];

fetch("/static/help_content.json")
  .then(res => res.json())
  .then(data => {
    helpData = data.help;
    renderHelp();
  });

const helpToggle = document.getElementById("help-toggle");
const helpPanel = document.getElementById("help-panel");
const helpQuestions = document.getElementById("help-questions");

helpToggle.addEventListener("click", () => {
  helpPanel.classList.toggle("hidden");
});

function renderHelp() {
  helpQuestions.innerHTML = "";

  helpData.forEach(item => {
    const btn = document.createElement("button");
    btn.className =
      "w-full text-left px-3 py-2 rounded-xl bg-[#2a2826] hover:bg-[#343230] transition";
    btn.innerText = item.question;

    btn.onclick = () => {
      helpPanel.classList.add("hidden");

      appendMessage("user-message-template", item.question);
      appendMessage("bot-message-template", item.answer);
    };

    helpQuestions.appendChild(btn);
  });
}
