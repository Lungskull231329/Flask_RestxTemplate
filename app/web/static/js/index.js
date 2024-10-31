const baseUrl = 'http://192.168.1.151:5000'


function getFiles() {

    fetch(baseUrl + '/file', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
    }).then(r => r.text().then(function (value) {
                filesList = JSON.parse(value)
                // console.log(filesList['list_files'])
                getToast('Успешно получены файлы', '')
                changeList(filesList['list_files']);
            }
        )
    )
}

function sendFile() {

    const input = document.querySelector('input[type="file"]');
    const data = new FormData();
    console.log(input.files)
    data.append('file', input.files[0])
    data.append('file_size', (input.files[0].size/1024/1024).toFixed(4))
    data.append('mime_type',input.files[0].type)

    let token = localStorage.getItem('token', data['token'])

    fetch(baseUrl + '/file', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + token
        },
        body: data
    })
        .then(r =>  r.json().then(data => ({status: r.status, body: data})))
        .then(obj => console.log(obj));
}

function changeList(textArr) {
    let tempText = "<ol class='list-group list-group-numbered'>"

    textArr.forEach(v => {tempText += `<li style="display: flex"
            class="list-group-item">Название файла: ${v['real_name']} Размер файла: ${v['size']} МБ            <button onClick="downloadFileFromURL('{{ action }}')" class="btn btn-success" type="submit">Скачать
            </button>            <button data-bs-target="#exampleModal" onClick="changeInfoModal('{{ action }}')" data-bs-toggle="modal"
                    class="btn btn-danger" type="button">Удалить            </button>
        </li>`
    })
    tempText += '</ol>'
    const divList = document.getElementById('list');
    divList.innerHTML = tempText;
}

function downloadFileFromURL(fileName) {
    let url = baseUrl + `/download/${fileName}`
    fetch(url,
        {method: 'GET'})
        .then(response => response.blob())
        .then(blob => {
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = fileName;
            link.click();
        })
        .catch(error => console.error('Error downloading file:', error));
}

function changeInfoModal(name){
    const btnDelete = document.getElementById('delete')
    btnDelete.value = name
}

function deliteFile(){

    const value = document.getElementById('delete')
    const urlDelete = baseUrl +"/delete"
    const data = value.value

    fetch(urlDelete, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(r => r.text().then(function (value) {
                filesList = JSON.parse(value)
                getToast('Успешно удалён файл:', filesList['message'])
                changeList(filesList['list_files']);
            }
        )
    )
}

function getToast(head, body) {

    const toast = document.getElementById('liveToast')

    const toastHead = document.getElementById('toast-head')
    toastHead.innerHTML = head

    const toastBody = document.getElementById('toast-body')
    toastBody.innerHTML = body

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toast)

    toastBootstrap.show()
}

async function getLogin() {

    let login = document.getElementById('login').value;
    let password = document.getElementById('password').value;
    data = {
        'login': login,
        'password': password
    }

    await fetch(baseUrl + '/login', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(r =>  r.json().then(data =>{

        if(data['token'] != null){
            getToast('Успешная авторизация', 'Поздравляем, вы вошли в систему')
            localStorage.setItem('token', data['token'])
            document.getElementById('contentHtml').style.removeProperty('display')
            document.getElementById('loginHtml').style.display = "none"
            getFiles()
        }
        else{
            getToast('Ошибка авторизации', 'Неверная пара логин/пароль')
        }
    }))
}

async function checkToken(){
    await fetch(baseUrl + '/login', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
    }).then(r =>  r.json().then(data =>{
        console.log(data)
        if(data['result'] === true){
            document.getElementById('contentHtml').style.removeProperty('display')
            document.getElementById('loginHtml').style.display = "none"
            getFiles()
        }
        else{
            document.getElementById('loginHtml').style.removeProperty('display')
            document.getElementById('contentHtml').style.display = "none"
        }
    }))
}

checkToken()

function logOut(){
    localStorage.removeItem('token')
    document.getElementById('loginHtml').style.removeProperty('display')
    document.getElementById('contentHtml').style.display = "none"
}

