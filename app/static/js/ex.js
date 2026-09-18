document.addEventListener('DOMContentLoaded', () => {
  // --- Seletores dos Elementos ---
  const circle = document.getElementById("breathCircle");
  const startBtn = document.getElementById("btnIniciar");
  const pauseBtn = document.getElementById("btnPausar");
  const terminateBtn = document.getElementById("btnTerminar");
  const timeDisplay = document.getElementById("tempoTotal");
  const exBox = document.querySelector('.ex-box');

  // --- Variáveis de Controle ---
  let timerInterval = null; // Guarda o intervalo do cronômetro
  let totalSeconds = 0;     // Conta o tempo total em segundos
  
  // Pega o ID do exercício do atributo data-*
  const exercicioId = exBox.dataset.exercicioId;

  // --- Funções de Animação ---
  function startBreathing() {
      if (!circle.classList.contains("animating")) {
          circle.classList.add("animating");
      }
  }

  function stopBreathing() {
      if (circle.classList.contains("animating")) {
          circle.classList.remove("animating");
      }
  }

  // --- Funções do Cronômetro ---
  function startTimer() {
      if (timerInterval) return; // Não inicia se já estiver rodando

      startBreathing(); // Inicia a animação junto com o timer

      timerInterval = setInterval(() => {
          totalSeconds++;
          const minutes = Math.floor(totalSeconds / 60).toString().padStart(2, '0');
          const seconds = (totalSeconds % 60).toString().padStart(2, '0');
          timeDisplay.textContent = `TEMPO TOTAL:  ${minutes}:${seconds}`;
      }, 1000);
  }

  function pauseTimer() {
      stopBreathing(); // Pausa a animação
      clearInterval(timerInterval); // Para o cronômetro
      timerInterval = null; // Limpa a variável de intervalo
  }

  async function terminateAndSave() {
      pauseTimer(); // Para tudo

      if (totalSeconds === 0) {
          alert("Nenhum tempo foi registrado. Complete pelo menos 1 segundo do exercício.");
          return;
      }

      // Prepara os dados para enviar ao servidor
      const praticaData = {
          id_exercicio: parseInt(exercicioId, 10),
          tempo_segundos: totalSeconds
      };

      try {
          // Envia os dados para a rota /salvar_pratica
          const response = await fetch('/salvar_pratica', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(praticaData),
          });

          const result = await response.json();

          if (result.success) {
              alert(result.message); // Exibe "Prática salva com sucesso!"
              // Redireciona para a página de histórico após salvar
              window.location.href = '/historico'; 
          } else {
              // Exibe a mensagem de erro vinda do servidor
              alert(`Erro ao salvar: ${result.message}`);
          }
      } catch (error) {
          console.error('Falha na comunicação com o servidor:', error);
          alert('Não foi possível salvar a prática. Verifique sua conexão.');
      }
  }

  // --- Adiciona os Eventos aos Botões ---
  startBtn.addEventListener("click", startTimer);
  pauseBtn.addEventListener("click", pauseTimer);
  terminateBtn.addEventListener("click", terminateAndSave);
});
