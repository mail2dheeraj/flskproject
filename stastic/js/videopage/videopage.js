// var connection = new WebSocket('ws://localhost:8000/');

 var canvas = document.getElementById("preview");
 var context = canvas.getContext('2d');
canvas.width = 900;
canvas.height = 700
// style="display:none;"

function Draw(video,context){
                context.drawImage(video,0,0,context.width,context.height);
$('#play').attr('src',canvas.toDataURL('image/webp'))
                // socket.emit('stream',canvas.toDataURL('image/webp'));
            }

var localVideoBlock = document.getElementById('local-video')
// var connection = io("ws://localhost:8000");
// var connection = new RTCPeerConnection() 
var connection = new WebSocket('ws://localhost:8000'); 
var sendingVideoData
var myConnection

connection.onopen = function () { 
   console.log("Connected"); 
connection.send('okk')
myConnection = new webkitRTCPeerConnection();
};
connection.onmessage = function (message) {
console.log(message)

}


myConnection.onicecandidate = function (event) { 
		
         if (event.candidate) { 
            send({ 
               type: "candidate", 
               candidate: event.candidate 
            }); 
         } 
      }; 


















// connection.on("connect", () => {

  // either with send()
  // socket.send("Hello!");
// console.log('connecte')
  // or with emit() and custom event names
  // socket.emit("salutations", "Hello!", { "mr": "john" }, Uint8Array.from([1, 2, 3, 4]));
// });
console.log('hii')
var localVideo;
function joinCall(){
navigator.getUserMedia({video:true,audio:true},(s)=>{
localVideo = s;
localVideoBlock.srcObject= localVideo;
document.getElementById('local-video').addEventListener('playing', () => {
  console.log('Video is now streaming!')
});
// console.log(localVideo)
// sendingVideoData = setInterval(()=>{
// connection.emit('connecteduser',{'name':'Dheeraj'});
// Draw(localVideoBlock,context)
// console.log('sending')
// },100)

// localVideo.getAudioTracks()[0].id
// localVideo.getVideoTracks()
// localVideo.getTracks()



},(err)=>{})


}




