//配置具体修改规则

// module.exports = function override(config, env) {
//     // do stuff with the webpack config...
//     return config;
// };



const { override, fixBabelImports, addLessLoader } = require('customize-cra');


module.exports = override(
    fixBabelImports('import', {
        libraryName: 'antd',
        libraryDirectory: 'es',
        style: true,
    }),
    addLessLoader({
        lessOptions: {
            javascriptEnabled: true, // 允许js修改主题色
            modifyVars: { '@primary-color': 'pink' }, //修改主颜色 默认#1DA57A
        }
    }),

    /*
    关于这个addLessLoader
    如果更换到低版本 yarn add less-loader@5.0.0 就不会报错
    写法
    addLessLoader({
        javascriptEnabled: true, // 允许js修改主题色
        modifyVars: { '@primary-color': 'pink' }, //修改主颜色 默认#1DA57A
    }),

    
    但是如果默认安装最新版本，写法如下
    addLessLoader({
        lessOptions:{
                javascriptEnabled: true, // 允许js修改主题色
                modifyVars: { '@primary-color': 'pink' }, //修改主颜色 默认#1DA57A
        }
    }),


    */

);
