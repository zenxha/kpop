var btn= document.getElementById("btn");
var input = document.getElementById("url");
var output = document.getElementById("demo"); 
var form = document.getElementById("form"); 
var urlInvalid = document.getElementById('urlInvalid')

function submit() {
    if(!input.startsWith('http')) {
        urlInvalid.style.display = 'block'
        console.log('invalid')
    }
    else {
        form.submit()
        console.log('valid')
    }
}