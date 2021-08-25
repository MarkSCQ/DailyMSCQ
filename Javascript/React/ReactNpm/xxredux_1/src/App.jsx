
import { Provider } from "react-redux";
import { applyMiddleware, createStore } from "redux";
import thunk from 'redux-thunk';

import reducer from "./Reducers/Reducer";
import Container from "./Components/Container";
import store from "./Stores/Store"
/**
 * store  存放数据的仓库
 * const store = createStore(reducer)
 *
 * state  数据的仓库 当中存储的数据
 * store.getState()
 *
 * action 对象 用来描述如何操作状态的
 * const action = {
 *  type:"AddOne",
 *  num:1
 * }
 *
 * dispatch 更改当前state的唯一方法
 * store.dispatch(action)
 *
 * reducer 函数 用来返回一个新的一个state 用来更新state
 * const reducer = (state=10,action)=>{
 * switch(action.type){
 * case action1:
 *  return ...
 * case action2:
 *  return ...
 * default：
 *  return ...
 * }
 * }
 */

// const store = createStore(math);

// console.log(store.dispatch(addAction(1)));
// console.log(store.getState());


function App() {

  console.log(store)

  return (
    <Provider store={store}>
      <Container />
    </Provider>
  );
}

export default App;
