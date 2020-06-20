
<html>
    <head>
        <title>Validity for mobile </title>
        <script type='text/javascript'>

//   \d= match any digit between 0 to 9
//    \w=matches any word character(a-z,A-Z,0-9,_)
//     \s=matches white  space (eg.space and character)
//      \t= match tab only


        function validate(){

             var text=document.getElementById('phone_no').value;
             //var reg=/a.b/ axxxb=allowed..it doesnt treat .as a dot so use \. 
              
            var reg=/^([a-zA-Z0-9\.-]+)@([a-zA-z0-9-]+).([a-zA-z]{2,20}).([a-zA-Z]{2,10})?$/    //^=starting and $=ending and abcd is invalid
            // + min one or more than 1
        //? entire is optional
          // {2,10}min=2 and max=10;
            //var reg=/abc/   abcd is valid
            if(reg.test(text)){

                document.getElementById('lbl').innerHTML='Valid';
                document.getElementById('lbl').style.visibility="visible";
                document.getElementById('lbl').style.color="green";

            }
            else{
                document.getElementById('lbl').innerHTML='InValid';
                document.getElementById('lbl').style.visibility="visible";
                document.getElementById('lbl').style.color="red";

                
            }


        }

</script> 

</head>
<body>

    <form>


        <input id="Phone_no" placeholder='Phone_no'  type="text"/><br>
         <label id='lbl'   style="color : red; visibility:hidden">Invalid</label>
         <br>
         <button onclick='validate()' , type='submit'>submit</button>

        </form>
        </body>
        </html>