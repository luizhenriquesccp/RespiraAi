function login(event) {
  event.preventDefault();
  const user = document.getElementById("user").value;
  const pass = document.getElementById("pass").value;

  if (user === "admin" && pass === "1234") {
    window.location.href = "index.html";
  } else {
    document.getElementById("erro").innerText = "Usuário ou senha incorretos!";
  }
}
