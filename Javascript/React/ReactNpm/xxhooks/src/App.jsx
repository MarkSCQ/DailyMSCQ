import { useState, useReducer } from 'react'




// 和类组件相似，更新state会刷新组件
function App() {
  /*
    set'State'方法
    // 当前state的值，setCount设置state中的count value
    const [count, setCount] = useState({ type: 'add', value: 0 })
  
    // notice: setState() is asynchronous hooks here is asynchronous
    const onCount = () => {
      // setCount(count + 1)
  
      setCount((prevState) => {
        if (prevState.type === 'add') {
          return { ...prevState, value: prevState.value + 1 }
        }
        return prevState
      })
      // setCount(count++) is not allowed, this setCount is equal to setCount(count=count+1)
    }
  */
  let reducerFn
  const [count, countDispatcher] = useReducer(reducerFn, 0)

  reducerFn = (prevState, action) => {
    switch (action.type) {
      case "add":
        return prevState + 2
      case "minus":
        return prevState - 2
      default:
        return prevState
    }
  }

  // useReducer 方法


  console.log(count)

  const addCount = (param) => {
    countDispatcher({ type: "add", value: 2 })
  }

  const minusCount = (param) => {
    countDispatcher({ type: "minus", value: 2 })
  }
  return (
    <div className="App">
      <h1>Hello Hooks</h1>

      <div>{count}</div>
      <div>
        {/* <input></input> */}
      </div>


      <button onClick={() => { addCount() }}>COUNT+2</button>
      <button onClick={() => { minusCount() }}>COUNT-2</button>
    </div>
  );
}

export default App;
