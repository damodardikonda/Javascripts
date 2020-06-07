let user={

    name:"damodar",
    roll:19,
    subject:"javascript",
    college:"gpp",
    school:"Ramanbaug",

    login:function(){
       
        console.log("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii");
        
    }
}

console.log(user.name)
console.log(user)

//user.college="zeal"
console.log(user.college)

console.log(user['name']);

const k='roll';

console.log(user['k']);

console.log(typeof(user));

user.login();