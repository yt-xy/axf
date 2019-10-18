function changeImage(){
    var i = document.getElementById('changeImg');
    i.src = '/axfuser/get_code/?'+Math.random();
}


function parse(){

    var password = document.getElementById('password').value;

    password = md5(password);

    document.getElementById('password').value = password;


    return true
}