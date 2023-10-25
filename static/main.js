document.querySelector("#submit_setor").addEventListener('click', function (event){
    nome = document.querySelector("#nome_setor").value.trim()
    
    if (!nome){
        alert("Campo vazio!")
        event.preventDefault()
    }

    document.querySelector("#nome_setor").value = nome
})