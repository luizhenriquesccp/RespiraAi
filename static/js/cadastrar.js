$(function () {
  $("#form-cadastro").on("submit", function (e) {
    e.preventDefault();

    let nome = $("#nome").val().trim();
    let email = $("#email").val().trim();
    let senha = $("#senha").val().trim();

    if (nome.length < 3) {
      $("#mensagem").text("O nome deve ter pelo menos 3 caracteres.");
      return;
    }
    if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
      $("#mensagem").text("E-mail inválido.");
      return;
    }
    if (senha.length < 5) {
      $("#mensagem").text("A senha deve ter pelo menos 5 caracteres.");
      return;
    }

    let usuarios = JSON.parse(localStorage.getItem("usuarios") || "[]");

    if (usuarios.some((u) => u.email === email)) {
      $("#mensagem").text("E-mail já cadastrado.");
      return;
    }

    usuarios.push({ nome, email, senha });
    localStorage.setItem("usuarios", JSON.stringify(usuarios));

    $("#mensagem")
      .css("color", "green")
      .text("Cadastro realizado com sucesso!");
    $("#form-cadastro")[0].reset();
  });
});
