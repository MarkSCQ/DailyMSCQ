class trafficLight {

    constructor(light, time) {
        this.light = light
        this.time = time
    }


    displayLight() {
        console.log(`This is ${this.light.toUpperCase()}`)
        // console.log(this)
    }


}


// traficLight.prototype.displayLight = function () {
//     console.log(`This is ${this.light.toUpperCase()}`)
//     console.log(this)
// }




const playLight = (lightObj) => {
    return new Promise(resolve => {
        setInterval(function () { console.log(lightObj.light); }, lightObj.time);
        setTimeout(() => {
            lightObj.displayLight()

            resolve()
        }, lightObj.time)
    })
}


const trafficSystem = () => {

    const redLight = new trafficLight("RED", 5000)
    const greenLight = new trafficLight("GREEN", 3000)
    const yellowLight = new trafficLight("YELLOW", 1000)
    console.log()
    console.log("----------------------------------------------")
    redLight.displayLight()
    greenLight.displayLight()
    yellowLight.displayLight()
    console.log("----------------------------------------------")
    console.log()

    const startSys = () => {
        Promise.resolve()
            .then((a) => {
                console.log("REDCLG")
                return playLight(redLight)
            })
            .then(() => {
                console.log("GREENCLG")
                return playLight(greenLight)

            })
            .then(() => {
                console.log("YELLOWCLG")
                return playLight(yellowLight)
            })
            .then(() => {
                return startSys()
            })
    }
    startSys()
}


function main() {

    trafficSystem()
}


main()



