
const navItems = document.querySelector('.nav-items')
const barsBtn = document.querySelector('.bars-btn')
const timesBtn = document.querySelector('.times-btn')
const body = document.querySelector('body')

const main = document.querySelector('main')


barsBtn.addEventListener('click', function() {
    barsBtn.style.display = 'none'
    timesBtn.style.display = 'inline-block'

    navItems.classList.add('show-nav-items')
    body.style.overflowY= 'hidden'
    // mobileSearchForm.style.display = 'block'

})

timesBtn.addEventListener('click', function() {
    barsBtn.style.display = 'inline-block'
    timesBtn.style.display = 'none'

    navItems.classList.remove('show-nav-items')
    body.style.overflowY = 'auto'
    // mobileSearchForm.style.display = 'none'
})

window.addEventListener('resize', function(){
    if(window.innerWidth >= 1000){
        barsBtn.style.display = 'inline-block'
        timesBtn.style.display = 'none'
        navItems.classList.remove('show-nav-items')
        body.style.overflowY = 'auto'
    }
})


const navContainer = document.querySelector('.nav-container')
console.log(navContainer.offsetHeight)

const searchForm = document.querySelector('#search-form')
const data = document.querySelector('#data')

searchForm.addEventListener('submit', function(event){
    event.preventDefault()
    const searched = data.value
    searchForm.reset()

    // window.location.href = `https://www.google.com/search?q=${data}`
    window.open(
        `https://www.google.com/search?q=${searched}`, '_blank'
    )
})

const mobileSearch = document.querySelector('#mobile-search')
const mobileData = document.querySelector('#mobile-data')

mobileSearch.addEventListener('submit', function(event){
    event.preventDefault()
    const searched = mobileData.value
    searchForm.reset()

    // window.location.href = `https://www.google.com/search?q=${data}`
    window.open(
        `https://www.google.com/search?q=${searched}`, '_blank'
    )
})

// change text size
const h1 = [...document.querySelectorAll('h1')]
const h2 = [...document.querySelectorAll('h2')]
const h3 = [...document.querySelectorAll('h3')]


window.addEventListener('scroll', function(){
    // location of the scroll bar
    console.log(window.pageYOffset)
})

// full html document height
console.log('Document Height:', document.body.scrollHeight)
// windows view port height (vh)
console.log('Window View Port Height:', window.innerHeight)
// element offset height
console.log('Main First Child Offset Height', main.children[0].offsetHeight)
// element client height
console.log('Main First Child Client Height', main.children[0].clientHeight)

