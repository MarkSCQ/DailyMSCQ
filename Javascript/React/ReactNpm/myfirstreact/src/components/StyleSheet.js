import React from 'react'
import './myStyles.css'
function StyleSheet(props) {
    let classname = props.primary?'primary':''
    return (
        <div>
            <h1 className={`${classname} font-xl`}>style sheet</h1>
        </div>
    )
}

export default StyleSheet
