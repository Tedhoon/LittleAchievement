document.querySelector('.dropdown').addEventListener('click', () => {
    document.querySelector('.dropdown_itembox').classList.toggle('show')
})

drop_item = document.querySelectorAll('.dropdown_item')


Array.from(drop_item).forEach(item => {
    item.addEventListener('click', () => {
        document.querySelector('.dropdown_display').innerHTML = this.event.target.innerHTML + '<span>▼</span>'
        document.querySelector('#id_tags').value = this.event.target.innerHTML
    })
})


document.querySelector('.dropdown2').addEventListener('click', () => {
    document.querySelector('.dropdown2_itembox').classList.toggle('show')
})

drop_item = document.querySelectorAll('.dropdown2_item')


Array.from(drop_item).forEach(item => {
    item.addEventListener('click', () => {
        document.querySelector('.dropdown2_display').innerHTML = this.event.target.innerHTML + '<span>▼</span>'
        document.querySelector('#id_period').value = parseInt(this.event.target.innerHTML)
    })
})