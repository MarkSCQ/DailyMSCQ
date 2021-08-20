const imgUrl = "https://randomuser.me/api/portraits/women/10.jpg"


const loadimage = (imgUrl) => {
    return new Promise((resolve, reject) => {
        let imgtag = document.createElement('img')

        imgtag.onload = () => {
            resolve(imgUrl)
        }
        imgtag.onerror = () => {
            reject("ERROR")
        }
        imgtag.src = imgUrl
        document.getElementById("imgdiv").appendChild(imgtag)
    })

}

loadimage(imgUrl)