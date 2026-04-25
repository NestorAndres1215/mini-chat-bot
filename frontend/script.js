function getTime() {
  return new Date().toLocaleTimeString('es', { hour: '2-digit', minute: '2-digit' });
}

function addMsg(text, type) {
  const chat = document.getElementById('chat');
  const initial = type === 'user' ? 'T' : 'B';
  const div = document.createElement('div');
  div.className = 'msg ' + type;
  div.innerHTML = `
    <div class="msg-avatar">${initial}</div>
    <div class="msg-wrap">
      <div class="bubble">${text}</div>
      <div class="msg-time">${getTime()}</div>
    </div>
  `;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function showTyping() {
  const chat = document.getElementById('chat');
  const div = document.createElement('div');
  div.className = 'msg bot';
  div.id = 'typing-indicator';
  div.innerHTML = `
    <div class="msg-avatar">B</div>
    <div class="msg-wrap">
      <div class="bubble" style="padding:10px 14px;">
        <div class="typing"><span></span><span></span><span></span></div>
      </div>
    </div>
  `;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function removeTyping() {
  const el = document.getElementById('typing-indicator');
  if (el) el.remove();
}

function enviar() {
  const input = document.getElementById('mensaje');
  const texto = input.value.trim();
  if (!texto) return;

  addMsg(texto, 'user');
  input.value = '';
  showTyping();

  fetch(`http://127.0.0.1:8000/chat?mensaje=${encodeURIComponent(texto)}`)
    .then(res => res.json())
    .then(data => {
      removeTyping();
      addMsg(data.respuesta, 'bot');
    })
    .catch(() => {
      removeTyping();
      addMsg('Error al conectar con el servidor.', 'bot');
    });
}

function sendQuick(text) {
  document.getElementById('mensaje').value = text;
  enviar();
}

document.getElementById('mensaje').addEventListener('keydown', e => {
  if (e.key === 'Enter') enviar();
});