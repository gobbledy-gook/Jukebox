var toggle = true
console.log('hello')
var playlist = document.getElementById('playlist_div1')

playlist.addEventListener('click', e => {
    if (toggle === true)
    {
        playlist.classList.add('playlist_enlarge')
        toggle = false
        console.log('toggle was true')
    } else {
        playlist.classList.remove('playlist_enlarge')
        toggle = true
        console.log('toggle was false')
    }
})