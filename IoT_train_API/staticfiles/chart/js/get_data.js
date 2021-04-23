

let datas = (url) =>{
    fetch(url, {
        method:"GET"
    }).then(response => response.json()
    ).then(json => console.log(json))
}

