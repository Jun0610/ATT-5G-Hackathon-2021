navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => { handlerFunction(stream) })


function handlerFunction(stream) {
  rec = new MediaRecorder(stream);
  rec.ondataavailable = e => {
    audioChunks.push(e.data);
    if (rec.state == "inactive") {
      let blob = new Blob(audioChunks, { type: 'audio/wav' });
      recordedAudio.src = URL.createObjectURL(blob);
      recordedAudio.controls = true;
      recordedAudio.autoplay = true;
      download.href = recordedAudio.src;
      download.download = 'wav';
      download.innerHTML = 'download';
      sendData(blob)
    }
  }
}
function sendData(data) { }

recordedAudio.onloadeddata = e => {
  document.getElementById("download").click();
}

record.onclick = e => {
  console.log('I was clicked')
  record.disabled = true;
  record.style.backgroundColor = "blue"
  stopRecord.disabled = false;
  audioChunks = [];
  rec.start();
}
stopRecord.onclick = e => {
  console.log("I was clicked")
  record.disabled = false;
  stop.disabled = true;
  record.style.backgroundColor = "red"
  rec.stop();
}