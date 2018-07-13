// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
//Edit entries
function onViewEntries(){
// document.getElementById('viewEntry').show;
    document.getElementById('viewEntry').style.display = 'inline';
    document.getElementById('newEntry').style.display = 'none';
    document.getElementById('modify').style.display = 'none';
    document.getElementById('reminder').style.display = 'inline';


}
//Create new entries
function onCreateEntries(){

//document.getElementById('newEntry').show;
document.getElementById('newEntry').style.display = 'inline';
document.getElementById('viewEntry').style.display = 'none';
document.getElementById('modify').style.display = 'none';
document.getElementById('reminder').style.display = 'inline';



}
//Modify all entries
function onModifyEntries(){
// document.getElementById('viewEntry').show;
    document.getElementById('viewEntry').style.display = 'none';
    document.getElementById('newEntry').style.display = 'none';
    document.getElementById('reminder').style.display = 'inline';
    document.getElementById('modify').style.display = 'inline';


}



