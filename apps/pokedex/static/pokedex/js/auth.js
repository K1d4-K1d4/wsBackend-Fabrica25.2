function getCookie(name) {
   let cookieValue = null;
   if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
         const cookie = cookies[i].trim();
         if (cookie.substring(0, name.length + 1) === (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
         }
      }
   }
   return cookieValue;
}

document.addEventListener('DOMContentLoaded', () => {
   const registerForm = document.getElementById('register-form');
   if (registerForm) {
      registerForm.addEventListener('submit', async function(event) {
         event.preventDefault();
         
         const form = event.target;
         const formData = new FormData(form);
         const data = Object.fromEntries(formData.entries());
         const messageDiv = document.getElementById('register-message');
         const csrfToken = getCookie('csrftoken');

         try {
               const response = await fetch('/api/register/', {
                  method: 'POST',
                  headers: {
                     'Content-Type': 'application/json',
                     'X-CSRFToken': csrfToken
                  },
                  body: JSON.stringify({ username: data.username, password: data.password })
               });

               if (response.ok) {
                  messageDiv.className = 'message success';
                  messageDiv.textContent = 'Conta criada com sucesso! Atualizando a página...';
                  setTimeout(() => window.location.reload(), 2000);
               } else {
                  const errorData = await response.json();
                  messageDiv.className = 'message error';
                  let errorMessage = 'Erro: ';
                  for (const key in errorData) {
                     errorMessage += `${key}: ${errorData[key].join(', ')} `;
                  }
                  messageDiv.textContent = errorMessage;
               }
         } catch (error) {
               messageDiv.className = 'message error';
               messageDiv.textContent = 'Ocorreu um erro de conexão.';
         }
      });
   }
});