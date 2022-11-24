const textarea = document.querySelector("textarea")
textarea.addEventListener("keyup", e =>{
    textarea.style.height = "59px"
    let scHeigh = e.target.scrollHeight
    textarea.style.height = `${scHeigh}px`
})