let timer = null;
let segundos = 0;
let pausado = false;

function atualizarTempo() {
  const min = String(Math.floor(segundos / 60)).padStart(2, "0");
  const sec = String(segundos % 60).padStart(2, "0");
  document.getElementById(
    "tempoTotal"
  ).innerText = `TEMPO TOTAL:  ${min}:${sec}`;
}

document.getElementById("btnIniciar").onclick = function () {
  if (!timer) {
    pausado = false;
    timer = setInterval(() => {
      if (!pausado) {
        segundos++;
        atualizarTempo();
      }
    }, 1000);
  } else {
    pausado = false;
  }
};

document.getElementById("btnPausar").onclick = function () {
  pausado = true;
};

document.getElementById("btnTerminar").onclick = function () {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
  pausado = false;
  // Salvar prática via AJAX
  const tempoFormatado = `${String(Math.floor(segundos / 60)).padStart(
    2,
    "0"
  )}:${String(segundos % 60).padStart(2, "0")}`;
  fetch("/salvar_pratica", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      exercicio: "{{ exercicio.nome }}",
      tempo: tempoFormatado,
    }),
  })
    .then((resp) => resp.json())
    .then((data) => {
      if (data.success) {
        alert("Prática salva com sucesso!");
        segundos = 0;
        atualizarTempo();
        window.location.href = "{{ url_for('historico') }}";
      } else {
        alert("Erro ao salvar prática: " + data.message);
      }
    })
    .catch(() => alert("Erro ao salvar prática."));
};
