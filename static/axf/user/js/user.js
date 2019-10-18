$(function () {
    $('#exampleInputName').blur(function () {
        //获取文本框的内容
        var name = $(this).val();
        // console.log(name);

        //校验文本框中的内容是否满足某条件
        var reg = /^[a-z]{3,6}$/;
        // console.log(reg);

        //test方法会判断某字符串是否符合某正则，如果符合返回的是true，不符合返回的是false
        b = reg.test(name);
        // console.log(b);

        if(b){
            // $('#nameinfo').html('用户名可使用').css({'color':'green','font-size':10});
            // $.getJSON(url,参数，function(data))
            $.getJSON('/axfuser/checkName/',
                {'name':name},
                function (data) {
                    if(data['status'] === 200){
                        $('#nameinfo').html(data['msg']).css({'color':'green','font-size':10});
                    }else{
                        $('#nameinfo').html(data['msg']).css({'color':'red','font-size':10});
                    }
                })
        }else{
            $('#nameinfo').html('*用户名格式错误').css({'color':'red','font-size':10});
        }
    });

    $('#exampleInputPassword2').blur(function () {
        //获取密码1
        var pwd1 = $('#password').val();
        // console.log(pwd1)
        //获取密码2
        var pwd2 = $(this).val();
        // console.log(pwd2)

        if(pwd1 === pwd2){
            $('#pwdinfo').html('*两次密码一致').css({'color':'green','font-size':10});
        }else{
            $('#pwdinfo').html('*两次密码不一致').css({'color':'red','font-size':10});
        }
    });

});

// function btn() {
//     var name = document.getElementById('exampleInputName');
//     var password1 = document.getElementById('password');
//     var password2 = document.getElementById('exampleInputPassword2');
//     var email = document.getElementById('exampleInputEmail1');
//
//     if(name || password1 || password2 || email === 0){
//         document.getElementById("btn").disabled=true;
//         // $('#btninfo').html('*不能有空').css({'color':'red','font-size':10});
//     }else{
//         document.getElementById("btn").disabled=false;
//         // $('#btn').attr("disabled",false);
//     }
// }

function parse1(){
    var password = document.getElementById('password').value;
    password = md5(password);
    document.getElementById('password').value = password;


    return true
}