const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnlogin-popup');
const iconClose = document.querySelector('.icon-close');


registerLink.addEventListener('click',()=>{
    wrapper.classList.add('active');
});

loginLink.addEventListener('click',()=>{
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click',()=>{
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
});

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    let email = document.querySelector('input[name="email"]').value;
    let password = document.querySelector('input[name="password"]').value;

    fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    }).then(response => response.json())
    .then(loginResponse => {
        console.log(loginResponse);
        if(loginResponse.success) {
            localStorage.setItem('parkingEmail', email);
            window.location.href = '/';
        }
    });
});


document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    let email = document.querySelector('input[name="email-signup"]').value;
    let fullname = document.querySelector('input[name="fullname-signup"]').value;
    let password = document.querySelector('input[name="password-signup"]').value;
    let confirmPassword = document.querySelector('input[name="confirmpassword-signup"]').value;

    if(password !== confirmPassword) {
        alert('Passwords do not match');
        return;
    }


    fetch('http://localhost:5000/api/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            password: password,
            fullname: fullname
        })
    }).then(response => response.json())
    .then(loginResponse => {
        console.log(loginResponse);
        if(loginResponse.success) {
            wrapper.classList.remove('active');
        }
    });
});