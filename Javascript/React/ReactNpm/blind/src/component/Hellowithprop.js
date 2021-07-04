// import { func } from 'prop-types'
import React from 'react'
import PropTypes from "prop-types";

function Hellowithprop(props) {

    return (<div><h1>caonima {props.name} id {props.id}</h1></div>)
}

Hellowithprop.propTypes={
    name:PropTypes.string.isRequired,
    id:PropTypes.number.isRequired
};


export default Hellowithprop