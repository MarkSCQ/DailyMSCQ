import axios from 'axios'


export const getAllData = (apiUrl) => {
    return axios.get(apiUrl)
}


export const getByDate = (apiUrl) => {
    return axios.get(apiUrl)
}

export const CharData = (apiurl, chartType) => {
    return axios.post(apiurl, {
        charttype: chartType
    })
}