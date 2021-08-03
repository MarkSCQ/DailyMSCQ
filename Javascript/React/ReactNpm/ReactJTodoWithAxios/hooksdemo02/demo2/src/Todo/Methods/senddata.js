import axios from 'axios'


export const addRecord = (url, date, content, price, tag) => {

    const [year, month, day] = date.split("-")
    console.log(year, month, day)
    return axios.post(url, {
        year: year,
        month: month,
        day: day,
        content: content,
        price: price,
        tag: tag
    })
}