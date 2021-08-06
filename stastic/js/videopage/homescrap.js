function sendUrl(){
// $('#basic-url').val();

$.ajax({
url:'/resiveScrapingUrl',
method: 'POST',
data:{'scrapingUrl':$('#basic-url').val(),
'matchFormat':$('#matchformat').val(),
'vs':$('#vs').val()
},
success: function(data){
console.log(data);
window.location=data.uri
},
error: function(err){
console.log(err)
}
})


} 