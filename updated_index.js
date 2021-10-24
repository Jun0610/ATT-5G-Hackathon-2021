//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;

var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input; 							//MediaStreamAudioSourceNode we'll be recording

// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record


var recordButton = document.getElementById("record");
var stopButton = document.getElementById("stopRecord");




//add events to those 2 buttons

recordButton.addEventListener("click", startRecording);

stopButton.addEventListener("click", stopRecording);


function startRecording() {
    console.log("recordButton clicked");
    var constraints = { audio: true, video: false }


    stopButton.disabled = false;


    navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
        console.log("getUserMedia() success, stream created, initializing Recorder.js ...");


        audioContext = new AudioContext();
        gumStream = stream;

        input = audioContext.createMediaStreamSource(stream);

        rec = new Recorder(input, { numChannels: 1 })


        rec.record()

        console.log("Recording started");
        stopButton.disabled = false;
        recordButton.disabled = true;

    })
}



function stopRecording() {
    console.log("stopButton clicked");

    //disable the stop button, enable the record too allow for new recordings

    stopButton.disabled = true;
    recordButton.disabled = false;

    //tell the recorder to stop the recording
    rec.stop();

    //stop microphone access
    gumStream.getAudioTracks()[0].stop();
    console.log("Mic Off")


    //create the wav blob and pass it on to createDownloadLink
    rec.exportWAV(createDownloadLink);

}

function createDownloadLink(blob) {
    var url = URL.createObjectURL(blob);
    var au = document.createElement('audio');
    var li = document.createElement('li');
    var link = document.createElement('a');


    //name of .wav file to use during upload and download (without extendion)
    var filename = new Date().toISOString();

    //add controls to the <audio> element
    au.controls = true;
    au.src = url;

    li.appendChild(au).autoplay = true;

    //add the filename to the li
    li.appendChild(document.createTextNode(filename + ".wav "))

    //add the save to disk link to li
    li.appendChild(link);

    recordingsList.appendChild(li);


    //save to disk link
    link.href = url;
    link.download = filename + ".wav"; //download forces the browser to donwload the file using the  filename
    link.innerHTML = "Save to disk";

    //add the new audio element to li

  
    document.getElementsByTagName('a').src = url;
   

}






