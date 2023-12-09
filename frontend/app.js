const droparea = document.querySelector('.droparea')
const btn = document.querySelector('.btn')
const output = document.querySelector('.output')
let image
let type

droparea.addEventListener('dragover', (e) => {
  e.preventDefault()
  droparea.classList.add('hover')
})

droparea.addEventListener('dragleave', () => {
  droparea.classList.remove('hover')
})

droparea.addEventListener('drop', (e) => {
  e.preventDefault()

  image = e.dataTransfer.files[0]
  type = image.type
  console.log(type)

  if (
    type == 'image/png' ||
    type == 'image/jpg' ||
    type == 'image/jpeg' ||
    type == 'image/bmp'
  ) {
    return upload(image)
  } else {
    droparea.setAttribute('class', 'droparea invalid')
    droparea.innerText = 'Invalid File Format!'
    return false
  }
})
// Authorization

const upload = (image) => {
  droparea.setAttribute('class', 'droparea valid')
  droparea.innerText = 'Added ' + image.name
}
btn.addEventListener('click', () => {
  const formData = new FormData()
  console.log(image)
  formData.append('image', image)
  fetch('http://127.0.0.1:5000/pre', {
    method: 'POST',
    body: formData,
  })
    .then((response) => response.json())
    .then((json) => {
      console.log(json)
      output.innerText = `User = ${json.response}`
      output.style.color = 'green'
    })
    .catch((err) => {
      output.innerText = 'error occured '
      output.style.color = 'red'
    })
})
