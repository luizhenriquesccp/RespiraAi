let timer = null;
let segundos = 0;
let pausado = false;

// Obter duração do exercício (em minutos)
const duracaoMin = parseInt(document.querySelector('.ex-box').dataset.duracao) || 0;
const duracaoSeg = duracaoMin * 60;

function atualizarTempo() {
  const min = String(Math.floor(segundos / 60)).padStart(2, "0");
  const sec = String(segundos % 60).padStart(2, "0");
  document.getElementById(
    "tempoTotal"
  ).innerText = `TEMPO TOTAL:  ${min}:${sec}`;
}

function terminarPratica(auto = false) {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
  pausado = false;
  const tempoFormatado = `${String(Math.floor(segundos / 60)).padStart(
    2,
    "0"
  )}:${String(segundos % 60).padStart(2, "0")}`;
  fetch("/salvar_pratica", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      exercicio: document.querySelector('.descricao-ex strong').innerText,
      tempo: tempoFormatado,
    }),
  })
    .then((resp) => resp.json())
    .then((data) => {
      if (data.success) {
        if (auto) {
          alert("Tempo finalizado! Prática salva com sucesso.");
        } else {
          alert("Prática salva com sucesso!");
        }
        segundos = 0;
        atualizarTempo();
        window.location.href = "/historico";
      } else {
        alert("Erro ao salvar prática: " + data.message);
      }
    })
    .catch(() => alert("Erro ao salvar prática."));
}

document.getElementById("btnIniciar").onclick = function () {
  if (!timer) {
    pausado = false;
    timer = setInterval(() => {
      if (!pausado) {
        segundos++;
        atualizarTempo();
        if (segundos >= duracaoSeg && duracaoSeg > 0) {
          terminarPratica(true);
        }
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
  terminarPratica(false);
};
