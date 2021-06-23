import React from 'react'
import Task from './Task'
const Thetask = ({ tasks }) => {

    return (
        <div>
            {tasks.map(
                (task) => (
                    <Task key={task.id} task={task} />
                )
            )}
        </div>
    )
}
// why there are two variables but one variable is used?

export default Thetask
