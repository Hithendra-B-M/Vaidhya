function login_fun() {
    var username = document.getElementById("login-username").value;
    var password = document.getElementById("login-password").value;

    if (!username || !password) {
        alert("Username and password are required.");
        return false;
    }

    return true;
}
