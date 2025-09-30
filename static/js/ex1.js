let timer = null;
let totalSeconds = 0;
const limite = 2 * 60; // 2 minutos em segundos

const tempoTotal = document.querySelector(".tempo-total");
const btnIniciar = document.querySelector(".btn-circular:nth-child(1)");
const btnPausar = document.querySelector(".btn-circular:nth-child(2)");
const btnTerminar = document.querySelector(".btn-retangular");

function formatarTempo(segundos) {
  const min = String(Math.floor(segundos / 60)).padStart(2, "0");
  const sec = String(segundos % 60).padStart(2, "0");
  return `${min}:${sec}`;
}

function atualizarTempo() {
  tempoTotal.innerHTML = `TEMPO TOTAL:&nbsp;&nbsp;${formatarTempo(
    totalSeconds
  )}`;
}

function iniciar() {
  if (timer) return;
  timer = setInterval(() => {
    if (totalSeconds < limite) {
      totalSeconds++;
      atualizarTempo();
    } else {
      clearInterval(timer);
      timer = null;
    }
  }, 1000);
}

function pausar() {
  clearInterval(timer);
  timer = null;
}

function terminar() {
  clearInterval(timer);
  timer = null;
  totalSeconds = 0;
  atualizarTempo();
}

btnIniciar.addEventListener("click", iniciar);
btnPausar.addEventListener("click", pausar);
btnTerminar.addEventListener("click", terminar);

// Inicializa o tempo zerado
atualizarTempo();
