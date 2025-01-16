function characterChance(){

       const images_fire = [
           '/static/img/azula.jpg',
           '/static/img/iroh.jpg',
           '/static/img/zuko.jpg',
       ];

       const images_water = [
           '/static/img/korra.png',
           '/static/img/katara.png',
           '/static/img/unalaq.png',
       ];

       const images_earth = [
           '/static/img/toff.png',
           '/static/img/bumi.png',
           '/static/img/daili.png',
           '/static/img/kioshi.png',
       ];

       const images_air = [
           '/static/img/aang.png',
           '/static/img/tenzin.png',
           '/static/img/zahir.png',
       ];

    let images = []

    const element = document.getElementById('element').innerText.trim().toLowerCase();

    switch (element){

        case 'fire':
            images = images_fire;
            break;

        case 'water':
            images = images_water;
            break;

        case 'air':
            images = images_air;
            break;

        case 'earth':
            images = images_earth;
            break;
    }

const random = Math.floor(Math.random() * images.length);
const image = images[random];

let imageElement = document.getElementById('image');
    if (!imageElement) {
        imageElement = document.createElement('img'); // Create an image element if it doesn't exist
        imageElement.id = 'image';
    }
imageElement.src = image;
imageElement.alt = 'random image';

document.getElementById('image-container').appendChild(imageElement);

}

window.onload = characterChance;