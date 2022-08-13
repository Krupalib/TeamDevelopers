scrollFunction()
 // window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  document.getElementById("navbar").style.top = "0";
  // if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0 || True) {
  //   document.getElementById("navbar").style.top = "0";
  // } else {
  //   document.getElementById("navbar").style.top = "-50px";
  // }
}
//
// console.log('Hello World')
//
//
//
//
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const handleStarSelect = (size) => {
    const children = form.children
    //console.log(children[0])
    for (let i=0; i < children.length; i++) {
        if(i <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
             handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'fourth': {
            handleStarSelect(4)
            return
        }
        case 'fifth': {
            handleStarSelect(5)
            return
        }
        default: {
            handleStarSelect(0)
        }
    }

}
//
// const getNumericValue = (stringValue) =>{
//     let numericValue;
//     if (stringValue === 'first') {
//         numericValue = 1
//     }
//     else if (stringValue === 'second') {
//         numericValue = 2
//     }
//     else if (stringValue === 'third') {
//         numericValue = 3
//     }
//     else if (stringValue === 'fourth') {
//         numericValue = 4
//     }
//     else if (stringValue === 'fifth') {
//         numericValue = 5
//     }
//     else {
//         numericValue = 0
//     }
//     return numericValue
// }
//
//
const arr = [one, two, three, four, five]
arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
       // console.log(event.target.id)
       handleSelect(event.target.id)

    }))
//
// arr.forEach(item=> item.addEventListener('click', (event)=>{
//     const val=event.target.id
//
//
//     let isSubmit = false
//     form.addEventListener('submit', e=> {
//
//       e.preventDefault()
//       if (isSubmit) {
//               return
//           }
//       isSubmit = true
//
//
//       // const id = e.target.id
//       // console.log((id))
//       // console.log((type(id)))
//       // const current_user = document.getElementById("current_user").value;
//       // console.log(id)
//
//       // const val_num = getNumericValue(val)
//
//
//       // $.ajax({
//       //
//       //   type : 'POST',
//       //   url : '/rating/',
//       //   data : {
//       //     'csrfmiddlewaretoken': csrf[0].value,
//       //     'el_id' : id,
//       //     'val' : val_num,
//       //     'current_user' : current_user,
//       //   },
//       //
//       //   success: function(response){
//       //     console.log(response)
//       //     confirmBox.innerHTML = `<h2>Successfully rated with ${response.score}</h2>`
//       //   },
//       //
//       //   error: function(error){
//       //               console.log(error)
//       //               confirmBox.innerHTML = '<h2>Ups... something went wrong</h2>'
//       //             }
//       // })
//     })
//   }))
