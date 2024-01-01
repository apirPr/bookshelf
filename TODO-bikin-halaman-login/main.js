const storageKey = 'STORAGE_KEY';
const apps = [];
const RENDER_EVENT = 'render-app';
const savedEvent = 'saved-book'



function generateId() {
    return +new Date();
}

function generateAppObject(id, title, author, year, isCompleted) {
    return {
        id,
        title,
        author,
        year,
        isCompleted,
    };
}

function makeApp(appObject, isSearchResult = false) {

    const {
        id,
        title,
        author,
        year,
        isCompleted
    } = appObject;

    const textTitle = document.createElement('h3');
    textTitle.innerText = `Judul: ${title}`;

    const textAuthor = document.createElement('p');
    textAuthor.innerText = `Penulis: ${author}`;

    const textYear = document.createElement('p');
    textYear.innerText = `Tahun: ${year}`;

    const textContainer = document.createElement('div');
    textContainer.classList.add('book_list');
    textContainer.append(textTitle, textAuthor, textYear);

    const container = document.createElement('article');
    container.classList.add('book_item');
    container.append(textContainer);
    container.setAttribute('id', `app-${id}`);

    if (isSearchResult) {
        const addButton = document.createElement('button');
        addButton.classList.add('green');
        addButton.innerText = 'Tambahkan ke rak';
        addButton.addEventListener('click', function () {
            addBookFromSearch(appObject);
        });
        container.append(addButton);
    } else {
        if (isCompleted) {
            const selesaiButton = document.createElement('button');
            selesaiButton.classList.add('green');
            selesaiButton.innerText = isCompleted ? 'belum dibaca' : 'sudah dibaca';
            selesaiButton.addEventListener('click', function () {
                selesaidiBaca(id);
            });

            const hapusButton = document.createElement('button');
            hapusButton.classList.add('red');
            hapusButton.innerText = 'hapus buku';
            hapusButton.addEventListener('click', function () {
                hapusbuku(id);
            });

            container.append(selesaiButton, hapusButton);

        } else {
            const belumButton = document.createElement('button');
            belumButton.classList.add('green');
            belumButton.innerText = isCompleted ? 'belum dibaca' : 'sudah dibaca';
            belumButton.addEventListener('click', function () {
                belumdiBaca(id);
            });

            const hapusButton = document.createElement('button');
            hapusButton.classList.add('red');
            hapusButton.innerText = 'hapus buku';
            hapusButton.addEventListener('click', function () {
                hapusbuku(id);
            });

            container.append(belumButton, hapusButton);

        }
    }


    return container
}

function addApp() {
    const title = document.getElementById('inputBookTitle').value;
    const author = document.getElementById('inputBookAuthor').value;
    const year = document.getElementById('inputBookYear').value;
    const finishRead = document.getElementById('inputBookIsComplete').checked;


    const generatedID = generateId();
    const appObject = generateAppObject(generatedID, title, author, year, finishRead);
    apps.push(appObject);

    document.dispatchEvent(new Event(RENDER_EVENT));
    saveData()
}

function findApp(appId) {
    for (appItem of apps) {
        if (appItem.id === appId) {
            return appItem;
        }
    }
    return null;
}

function findAppIndex(appId) {
    for (let i = 0; i < apps.length; i++) {
        if (apps[i].id === appId) {
            return i;
        }
    }
    return -1;
}

function isStorageExist() {
    try {
        if (typeof (Storage) === undefined) {
            throw new Error("browser kamu tidak mendukung local storage");
        }
        return true;
    } catch (error) {
        console.error("Kesalahan:", error.message);
        return null;
    }
}

function saveData() {
    if (isStorageExist()) {
        const parsed = JSON.stringify(apps);
        localStorage.setItem(storageKey, parsed);
        document.dispatchEvent(new Event(savedEvent));
    }
}

function loadDataFromStorage() {
    const serializedData = localStorage.getItem(storageKey);
    let data = JSON.parse(serializedData);

    if (data !== null) {
        for (const app of data) {
            apps.push(app);
        }
    }

    document.dispatchEvent(new Event(RENDER_EVENT));
}



function selesaidiBaca(appId) {
    const appTargetIndex = findAppIndex(appId);
    if (appTargetIndex === -1) return;

    const appToMove = apps[appTargetIndex];
    appToMove.isCompleted = false;

    apps.splice(appTargetIndex, 1);

    apps.push(appToMove);

    document.dispatchEvent(new Event(RENDER_EVENT));
    saveData()
}

function belumdiBaca(appId) {
    const appTargetIndex = findAppIndex(appId);
    if (appTargetIndex === -1) return;

    const appToMove = apps[appTargetIndex];
    appToMove.isCompleted = true;


    apps.splice(appTargetIndex, 1);


    apps.push(appToMove);

    document.dispatchEvent(new Event(RENDER_EVENT));
    saveData()
}

function hapusbuku(appId) {
    const appTargetIndex = findAppIndex(appId);
    if (appTargetIndex === -1) return;

    apps.splice(appTargetIndex, 1);
    document.dispatchEvent(new Event(RENDER_EVENT));
    saveData()
}



function searchBooks() {
    const nyari = document.getElementById('searchBookTitle').value.toLowerCase();
    const hasilNyari = document.getElementById('hasilNyari');

    const searchResults = apps.filter(app => app.title.toLowerCase().includes(nyari));

    if (searchResults.length === 0) {
        alert('Buku tidak terdaftar!');
        hasilNyari.innerHTML = '';
    } else {
        hasilNyari.innerHTML = '';

        for (const result of searchResults) {
            const resultElement = makeApp(result, true);
            hasilNyari.append(resultElement);
        }
    }
}


function addBookFromSearch(appObject) {
    apps.push(appObject);
    document.dispatchEvent(new Event(RENDER_EVENT));
    alert('Buku berhasil ditambahkan ke rak!');
}

function hapusHasilPencarian() {
    const hasilNyari = document.getElementById('hasilNyari');
    hasilNyari.innerHTML = '';
}



document.addEventListener('DOMContentLoaded', function () {
    const inputSubmitForm = document.getElementById('inputBook');
    inputSubmitForm.addEventListener('submit', function (event) {
        event.preventDefault();
        addApp();
    });
    if (isStorageExist()) {
        loadDataFromStorage();
    }
});

document.addEventListener(RENDER_EVENT, function () {
    const belumBaca = document.getElementById('incompleteBookshelfList');
    const sudahBaca = document.getElementById('completeBookshelfList');


    belumBaca.innerHTML = '';
    sudahBaca.innerHTML = '';

    for (const appItem of apps) {
        const appElement = makeApp(appItem);
        if (!appItem.isCompleted) {
            belumBaca.append(appElement);
        } else {
            sudahBaca.append(appElement);
        }
    }
});

document.getElementById('inputBook').addEventListener('submit', function (event) {
    const inputSubmit = document.getElementById('bookSubmit');

    if (inputSubmit) {
        alert('Anda telah menambahkan data buku :D');
    }
    event.preventDefault();
});


document.getElementById('searchBook').addEventListener('submit', function (event) {
    const nyari = document.getElementById('searchBookTitle').value.toLowerCase();
    event.preventDefault();

    const searchResults = apps.filter(app => app.title.toLowerCase().includes(nyari));

    if (searchResults.length === 0) {
        alert('Buku tidak terdaftar!');
    } else {
        searchBooks();
    }
});

document.addEventListener(savedEvent, () => {
    console.log('Data berhasil di simpan.');
});