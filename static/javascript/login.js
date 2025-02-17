function login(){
username=document.getElementById('u').value
password=document.getElementById('p').value
x=username.match(/Vijay kumar/g)
y=password.match(/9741334784/g)
if(username=='' || username==null){
    alert('enter any name')
    return false
}
else if(password==''||password==null){
    alert('enter any password')
     return false
}
else if(x==''|| x==null){
    alert('enter valid username')
    return false
}
else if(y==''|| y==null){
    alert('enter valid password')
    return false
}

}