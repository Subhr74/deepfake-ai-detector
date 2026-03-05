async function detectImage(){

const file=document.getElementById("fileInput").files[0]

const formData=new FormData()

formData.append("file",file)

const res=await fetch("http://127.0.0.1:5000/detect-image",{

method:"POST",
body:formData

})

const data=await res.json()

document.getElementById("result").innerText=data.result

document.getElementById("heatmap").src=data.heatmap

}

async function detectVideo(){

const file=document.getElementById("fileInput").files[0]

const formData=new FormData()

formData.append("file",file)

const res=await fetch("http://127.0.0.1:5000/detect-video",{

method:"POST",
body:formData

})

const data=await res.json()

document.getElementById("result").innerText=data.result

}