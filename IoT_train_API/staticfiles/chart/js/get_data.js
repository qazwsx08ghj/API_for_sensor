
// GET data by url
let get_data = (url) =>{
    return fetch(url).then(response =>
        response.json()
    )
}
