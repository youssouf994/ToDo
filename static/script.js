$(document).ready(function () {
    const panoramicaContainer = $(".panoramica-container");
    const panoramica = $(".panoramica");
    const prevButton = $(".indietro");
    const nextButton = $(".avanti");

    const itemWidth = 300; // Larghezza di un elemento "prodotto"
    const itemsPerPage = 4; // Numero di elementi da mostrare per pagina
    let currentPage = 1;

    function showPage(page) {
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;

        const prodotti = $(".prodotto");

        prodotti.each(function (index, element) {
            if (index >= startIndex && index < endIndex) {
                $(element).show();
            } else {
                $(element).hide();
            }
        });
    }

    prevButton.on("click", function () {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    nextButton.on("click", function () {
        const prodotti = $(".prodotto");
        const totalItems = prodotti.length;
        const totalPages = Math.ceil(totalItems / itemsPerPage);

        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
        }
    });

    showPage(currentPage);
});


//----------------------------------------------------------------------------------------------

$(document).ready(function () {
    // Mostra il div associato al pulsante cliccato
    $(".link").on("click", function () {
        var targetDiv = $(this).data("target");
        $("#" + targetDiv).show();
    });

    // Nascondi il div associato al pulsante di chiusura cliccato
    $(".chiudi_div").on("click", function () {
        var targetDiv = $(this).data("target");
        $("#" + targetDiv).hide();
    });

    // Nascondi il div se si clicca al di fuori di esso
    $(document).on("click", function (event) {
        $(".link").each(function () {
            var targetDiv = $(this).data("target");
            if (!$(event.target).closest("#" + targetDiv + ", .link[data-target='" + targetDiv + "']").length) {
                $("#" + targetDiv).hide();
            }
        });
    });
});


//});


//---------------------------------------------------------------------------------------------

$(document).ready(function () {
    const panoramicaContainer = $(".panoramica-container");
    const panoramica = $(".panoramica");
    const prevButton = $("#indietro");
    const nextButton = $("#avanti");

    const itemWidth = 300; // Larghezza di un elemento "prodotto"
    const itemsPerPage = 4; // Numero di elementi da mostrare per pagina
    let currentPage = 1;

    function showPage(page) {
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;

        const prodotti = $(".prodotto");

        prodotti.each(function (index, element) {
            if (index >= startIndex && index < endIndex) {
                $(element).show();
            } else {
                $(element).hide();
            }
        });
    }

    prevButton.on("click", function () {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    nextButton.on("click", function () {
        const prodotti = $(".prodotto");
        const totalItems = prodotti.length;
        const totalPages = Math.ceil(totalItems / itemsPerPage);

        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
        }
    });

    showPage(currentPage);
});


//---------------------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
    // Utilizzo dei dati passati dal file HTML
    let ingredienti = ingredienteA;
    let grafico = document.getElementById('grafico');
    let totale = totaleA;

    // Mappa degli ingredienti con percentuale di costo
    let costoIngreMap = ingredienti.map(ingre => ({
        ...ingre,
        percent: (ingre[7] / totale) * 100
    }));

    // Creazione dei div per ogni ingrediente
    costoIngreMap.forEach(ingre => {
        let divCostoSingolo = document.createElement('div');
        divCostoSingolo.classList.add('ingre');
        divCostoSingolo.style.height = `${ingre.percent}%`;
        divCostoSingolo.style.backgroundColor = 'yellow'; // Cambia il colore se necessario
        divCostoSingolo.style.borderStyle = 'solid';
        divCostoSingolo.style.borderColor = 'black';
        divCostoSingolo.style.borderWidth = '1px';
        grafico.appendChild(divCostoSingolo);
    });
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

$(document).ready(function () {
    // Seleziona gli elementi pop-up e i pulsanti
    const popup = $('#popupForm');  // Usa jQuery per selezionare l'elemento
    const openPopupButtons = $('.open-popup');  // Seleziona tutti i pulsanti con la classe "open-popup"
    const closePopup = $('.close-popup');  // Seleziona il bottone "X" per chiudere il pop-up

    // Apre il pop-up quando si clicca il bottone "Modifica"
    openPopupButtons.each(function () {
        $(this).on('click', function () {
            const taskId = $(this).data('id');  // Ottieni l'id della task dal data-id
            // Inserisci il valore dinamico della task da modificare nel form se necessario
            popup.css('display', 'flex');  // Mostra il pop-up
        });
    });

    // Chiude il pop-up quando si clicca il pulsante "X"
    closePopup.on('click', function () {
        popup.css('display', 'none');  // Nasconde il pop-up
    });

    // Chiude il pop-up se si clicca al di fuori del contenuto
    $(window).on('click', function (event) {
        if ($(event.target).is(popup)) {
            popup.css('display', 'none');  // Nasconde il pop-up se si clicca fuori
        }
    });
});

