import React from 'react'
import PropTypes from "prop-types";


const Hellobracketwithprop = (props) => {
    return <div><h1>fk cnm {props.name} - {props.id} </h1></div>
}


Hellobracketwithprop.propTypes={
    name:PropTypes.string.isRequired,
    id:PropTypes.number.isRequired
}

export default Hellobracketwithprop