const buttons = document.querySelectorAll(".quiz>button");
function disable() {
  buttons.forEach((b) => b.setAttribute("disabled", true));
}
buttons.forEach((b) => b.addEventListener("click", disable));
