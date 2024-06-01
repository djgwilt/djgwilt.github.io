function login() {
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var month = document.getElementById("month").value;
    var secret = document.getElementById("secret").value;

    var name = secret + fname + month + lname;
    name = name.replace(/\s/g, '');
    name = name.toLowerCase();
    var hash = CryptoJS.SHA1(name);
    document.getElementById("uname").href = "./logins/" + hash + ".html";

    name = secret + lname + month + fname;
    name = name.replace(/\s/g, '');
    name = name.toLowerCase();
    hash = CryptoJS.SHA1(name);
    document.getElementById("pwd").href = "./logins/" + hash + ".html";

    document.getElementById("uname").style.display = "block";
    document.getElementById("pwd").style.display = "block";
    document.getElementById("oucc").style.display = "block";
}
