function characterChance(){
       const images = [
           '/static/img/azula.jpg',
           '/static/img/iroh.jpg',
           '/static/img/zuko.jpg',
       ];

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