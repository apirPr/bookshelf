const registeredUsers = [
    { username: 'user1', password: 'pass1' },
    { username: 'user2', password: 'pass2' },
    // Tambahkan pengguna lain jika diperlukan
];

function validateSignup() {
    let username = document.getElementById('signupUsername').value;
    let email = document.getElementById('signupEmail').value;
    let password = document.getElementById('signupPassword').value;
    let confirmPassword = document.getElementById('confirmPassword').value;

    if (username === '' || email === '' || password === '' || confirmPassword === '') {
        alert('Semua kolom harus diisi');
        return false;
    }

    if (password !== confirmPassword) {
        alert('Password dan Konfirmasi Password harus sama');
        return false;
    }

    alert('Pendaftaran berhasil! Data telah ditambahkan.');


    resetSignupForm();
}

function validateLogin() {
    let username = document.getElementById('loginUsername').value;
    let password = document.getElementById('loginPassword').value;

    if (username === '' || password === '') {
        alert('Semua kolom harus diisi');
        return false;
    }

    // Simulasi verifikasi username dan password
    if (username === 'user' && password === 'password') {
        alert('Login berhasil! Selamat datang, ' + username);

        // Redirect ke halaman index.html
        window.location.href = '../../templates/index.html';
    } else {
        alert('Username atau password salah. Silakan coba lagi.');
    }

    // Reset formulir setelah login berhasil atau gagal
    resetLoginForm();
}

function resetSignupForm() {
    document.getElementById('signupUsername').value = '';
    document.getElementById('signupEmail').value = '';
    document.getElementById('signupPassword').value = '';
    document.getElementById('confirmPassword').value = '';
}

function resetLoginForm() {
    document.getElementById('loginUsername').value = '';
    document.getElementById('loginPassword').value = '';
}
