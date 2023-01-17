const container = document.querySelector('.container')
const cbBtn = document.querySelector('#cb-btn')

const colors = ['orange', 'purple', 'blue', 'red']
let index = 0

container.style.background = colors[index]

cbBtn.addEventListener('click', changeBackground)

function changeBackground(event) {
    if(index == colors.length-1) {
        index = 0
    }
    else if(index < colors.length) {
        index ++
    }
    container.style.background = colors[index]
}
