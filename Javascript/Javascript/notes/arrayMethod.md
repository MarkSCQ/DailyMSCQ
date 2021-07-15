```
const items = [
    {name:'bike'        ,price:100 },
    {name:'tv'          ,price:200 },
    {name:'album'       ,price:10 },
    {name:'book'        ,price:5 },
    {name:'phone'       ,price:500 },
    {name:'pc'          ,price:1000 },
    {name:'keyboard'    ,price:25 }
]
```



## array.map() take one old array and convert it into a new array with difference
```
const newarray = items.map((item)=>{
    return item.name
})
```



## array.filter() filter out the items when the return statement is true
```
const newarray = items.map((item)=>{
    return price>=100
})
```



## array.find() find an single object of one array, return the first item with is true of the return statement
```
const item = items.map((item)=>{
    return item.name === 'book'
})
```



## array.forEach() similar to for loop
```
items.forEach((item)=>{
    console.log(item.name)
    return item.price=10
})
```



## array.some() method determines whether at least one element of the array matches the given predicate
```
const hasInexpensiveItems = items.some((item)=>{
    return item.price<100
    })
```



## array.every() method determines whether all elements of the array match the predicate:
```
const hasInexpensiveItems = items.every((item)=>{
    return item.price<100
    })
```



## array.reduce(a,b) first arg, will be the previous iteration return and the second arg will be the current item.
```
const hasInexpensiveItems = items.reduce((currentTotal,item)=>{
    return item.price+currentTotal
    },0)

// Arrow function
reduce((accumulator, currentValue) => { ... } )
reduce((accumulator, currentValue, index) => { ... } )
reduce((accumulator, currentValue, index, array) => { ... } )
reduce((accumulator, currentValue, index, array) => { ... }, initialValue)

```



## array.includes() whether one element is inclued in the array
```
const items = [1,2,3,4,5]
const includesTwo = items.include(2)// return true
```
