let offset = 0;
const limit = 6;
const cardContainer = document.getElementById('content-container');

async function loadMoreCards() {
    try {
        const response = await fetch('/get__card');
        const data = await response.json();

        data.forEach(card => {
            const cardToken = document.createElement('div');
            cardToken.className = 'card__token';

            // Crear la imagen y configurarla
            const imgCard = document.createElement('img');
            imgCard.className = 'img__card';
            imgCard.setAttribute('src', card.url);
            imgCard.alt = 'image of token';

            // Agregar la imagen al contenedor principal
            cardToken.appendChild(imgCard);

            // Crear el contenedor de texto
            const containerCardText = document.createElement('div');
            containerCardText.className = 'container__card__text';

            // Crear y agregar el título
            const h3Title = document.createElement('h3');
            h3Title.textContent = card.title;
            containerCardText.appendChild(h3Title);

            // Crear y agregar el párrafo de la colección
            const pCollection = document.createElement('p');
            pCollection.className = 'p__collection';
            pCollection.textContent = card.collection;
            containerCardText.appendChild(pCollection);

            // Crear y agregar el párrafo de la descripción
            const pDescription = document.createElement('p');
            pDescription.className = 'p__description';
            pDescription.textContent = card.description;
            containerCardText.appendChild(pDescription);

            // Crear y agregar el párrafo del precio
            const pPrice = document.createElement('p');
            pPrice.className = 'p__price';
            pPrice.textContent = `Price: $${card.price}.00`;
            containerCardText.appendChild(pPrice);

            const formBuy = document.createElement('form');
            formBuy.className = 'form__buy';
            formBuy.setAttribute('action', "/buy__token");
            formBuy.setAttribute("method","POST")

            const hiddenKey = document.createElement('input');
            hiddenKey.className = 'hidden__key';
            hiddenKey.setAttribute('type', "hidden");
            hiddenKey.setAttribute("name","hidden__key")
            hiddenKey.setAttribute("value", card.key)

            formBuy.appendChild(hiddenKey);

            // Crear y agregar el botón de compra
            const buttonBuyToken = document.createElement('button');
            buttonBuyToken.className = 'button__buy__token';
            buttonBuyToken.textContent = 'Buy';
            buttonBuyToken.setAttribute("type","submit")
            formBuy.appendChild(buttonBuyToken);

            // Agregar el contenedor de texto al contenedor principal
            containerCardText.appendChild(formBuy)
            cardToken.appendChild(containerCardText);

            cardContainer.appendChild(cardToken);
        });

        offset += limit;
    } catch (error) {
        console.error('Error al cargar más tarjetas:', error);
    }
}

function handleScroll() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 500) {
        loadMoreCards();
    }
}

window.addEventListener('scroll', handleScroll);

// Cargar las primeras tarjetas al iniciar
loadMoreCards();