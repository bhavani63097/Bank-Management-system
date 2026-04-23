function handleLogin(event) {
  event.preventDefault();
  const username = document.getElementById('u').value.trim();
  const password = document.getElementById('p').value.trim();
  const errorDiv = document.getElementById('error-msg');
  const errorText = document.getElementById('error-text');

  if (!username || !password) {
    errorText.textContent = 'Please enter both username and password.';
    errorDiv.classList.remove('d-none');
    return false;
  }

  if (username !== 'admin' || password !== 'admin123') {
    errorText.textContent = 'Invalid username or password.';
    errorDiv.classList.remove('d-none');
    return false;
  }

  // Valid credentials — redirect to admin dashboard
  window.location.href = '/dash/';
  return false;
}