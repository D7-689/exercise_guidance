const captureVideoButton =document.querySelector('#video-button'); // Next button
const registerButton = document.querySelector('#register-button');
const video = document.querySelector('#screenshot-video');
const image_hidden = document.querySelector('#id_image');
const constraints = {
    video: true
  };


document.getElementById("screenshot-video").style.display ="none"; // 隱藏 video html
// document.getElementById("four_field").style.display ="block";   

captureVideoButton.onclick = function() {
    captureVideoButton.setAttribute('style','display: none;');  // 隱藏 Next button
    registerButton.removeAttribute("style");              // show 番 register button 出來
    document.getElementById("screenshot-video").style.display = "block"; // show 番 video html 出來
    // document.getElementById("four_field").style.display ="none";
    navigator.mediaDevices.getUserMedia(constraints).   //會提示使用者是否給予存取多媒體數據的許可 (是否允許使用camera 的信息)
    then(handleSuccess).catch(handleError);
};

registerButton.onclick = video.onclick = function() {
    var canvas = document.createElement("canvas");
    canvas.setAttribute('width','1024px');
    canvas.setAttribute('height','683px');
    canvas.getContext('2d').drawImage(video, 0, 0, 1024, 683);     //https://developer.mozilla.org/zh-CN/docs/Web/API/CanvasRenderingContext2D/drawImage 
    image_hidden.value = canvas.toDataURL();                                          //canvas.width, canvas.heigh
    document.forms["face-register-form"].submit();
};

function handleSuccess(stream) {
    registerButton.disabled = false;
    video.srcObject = stream;
}