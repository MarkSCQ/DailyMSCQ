import moment from 'moment'


export const DateDetail = (date) => {
    return moment(date).format('LL')
}


export const DateYMD = (date) => {
    return moment(date).format("YYYY-MM-DD");
}


export const DateCalendar = (date) => {
    return moment(date).calendar();
}



