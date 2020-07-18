const dropdown1 = document.querySelector('.dropdown')
const dropdown1_itembox = document.querySelector('.dropdown_itembox')
const dropdown1_item = document.querySelectorAll('.dropdown_item')
const dropdown1_display = document.querySelector('.dropdown_display')
const hidden_tag_value = document.querySelector('#id_tags')


const dropdown2 = document.querySelector('.dropdown2')
const dropdown2_itembox = document.querySelector('.dropdown2_itembox')
const dropdown2_item = document.querySelectorAll('.dropdown2_item')
const dropdown2_display = document.querySelector('.dropdown2_display')
const hidden_period_value = document.querySelector('#id_period')

const is_list = document.querySelector('#id_is_list')
const toggle_btn = document.querySelector("#toggle_btn")
const task_list_area = document.querySelector("#task_list_area")


dropdown1.addEventListener('click', ()=>{
    dropdown1_itembox.classList.toggle('show')
})

Array.from(dropdown1_item).forEach(item => {
    item.addEventListener('click',  ()=>{
        dropdown1_display.innerHTML = this.event.target.innerHTML + '<span>▼</span>'
        hidden_tag_value.value = this.event.target.innerHTML
    })
})


dropdown2.addEventListener('click',  ()=>{
    dropdown2_itembox.classList.toggle('show')
})

Array.from(dropdown2_item).forEach(item => {
    item.addEventListener('click',  ()=>{
        dropdown2_display.innerHTML = this.event.target.innerHTML + '<span>▼</span>'

        day_num = parseInt(this.event.target.innerHTML)
        hidden_period_value.value = day_num

        if (is_list.checked === true){
            make_task_list(day_num)
        }
    })
})


is_list.addEventListener('change', function (){
    
    if (this.checked) {
        toggle_btn.innerHTML = "多"
        make_task_list(hidden_period_value.value)

    } else {
        toggle_btn.innerHTML = "少"
        task_list_area.innerHTML = ""
    }
})

const make_task_list = function(num){
    let temp_html=""
    for (let i = 0; i < num; i++) {
        console.log(i, "<============")
        temp_html += "<label>" + (i + 1) + "일 째" + "</label>" + "<input type='text' name='tasklist" + i + "'/><br>"
    }
    
    task_list_area.innerHTML = temp_html
}