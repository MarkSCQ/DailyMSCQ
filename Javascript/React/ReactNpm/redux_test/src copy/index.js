import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

import { Provider } from 'react-redux'
import store from './redux/Store'


ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>
  ,
  document.getElementById('root')
);


// 检测redux中状态的改变，如果redux中状态发生改变，那么中心渲染app组件
// ! 使用了react-redux 不适用检测仍然可以更新。不容自行监测。connect是关键。connect默认可以检测redux中state
// store.subscribe(() => {
//   ReactDOM.render(
//     <App />,
//     document.getElementById('root')
//   );
// })
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
