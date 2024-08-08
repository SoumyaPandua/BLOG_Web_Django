const passwordInput = document.getElementById("password");
const passToggleBtn = document.getElementById("pass-toggle-btn");

passToggleBtn.addEventListener('click', () => {
    passToggleBtn.className = passwordInput.type === "password" ? "fa-solid fa-eye-slash" : "fa-solid fa-eye";
    passwordInput.type = passwordInput.type === "password" ? "text" : "password";
});

const confirmPasswordInput = document.getElementById("confirm-password");
const confirmPassToggleBtn = document.getElementById("confirm-pass-toggle-btn");

confirmPassToggleBtn.addEventListener('click', () => {
    confirmPassToggleBtn.className = confirmPasswordInput.type === "password" ? "fa-solid fa-eye-slash" : "fa-solid fa-eye";
    confirmPasswordInput.type = confirmPasswordInput.type === "password" ? "text" : "password";
});

document.getElementById('send-button').addEventListener('click', function() {
    document.getElementById('otp-group').style.display = 'block';
  });
  