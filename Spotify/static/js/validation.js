document.getElementById('registerForm').addEventListener('submit', function(event) {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    if (password !== confirmPassword) {
        event.preventDefault();
        alert('Las contraseñas no coinciden. Por favor, intenta de nuevo.');
    }
});
