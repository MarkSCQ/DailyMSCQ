import axios from 'axios'


export const addRecord = (url, id, date, content, price) => {

    const [year, month, day] = date.split("-")

    return axios.post(url, {
        year: year,
        month: month,
        day: day,
        id: id,
        content: content,
        price: price
    })
}