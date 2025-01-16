function validateForm(){
    const elementInput = document.getElementById('element').value.toLowerCase();
    const emojiInput = document.getElementById('emojis').value.toLowerCase();

    if(elementInput !== emojiInput){
        alert("Element and emoji must match");
        return false;
    }
    return true;
}