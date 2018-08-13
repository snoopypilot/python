/*
if(typeof names != 'undefined') {
    var name = JSON.parse(localStorage.getItem('names'));
    for(i=0; i<10; i++) {
        document.getElementById(i).value = name[i];
    }
}
*/
function submitted() {
    var name = ['A', 'B'];
    alert(name.length);
/*
    for(i=0; i<10; i++) {
        //name[i] = document.getElementById('1').value;
        alert(name[i]);
    }
    localStorage.setItem("names", JSON.stringify(name));

    location.reload();
    return false;
*/
}
