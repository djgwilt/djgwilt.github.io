// $('#RacingTrack2').ready(function() {
//     console.log('ready js')
// });

function storageChange(num) {
    let keyStatus = document.getElementById('keyStatus').innerHTML
    localStorage.setItem('keyStatus', num)
    checkStorage()
} 
// setInterval(storageChange() , 400);

function checkStorage() {
    let keyStatus = localStorage.getItem('keyStatus')
    if (keyStatus != null) {
        document.getElementById('keyStatus').innerHTML = keyStatus
    }
    
}