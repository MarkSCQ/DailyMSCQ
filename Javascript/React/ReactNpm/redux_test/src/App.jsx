import React from 'react'
import HookCounterOne from './components/HookCounterOne'
import HookCounter from './components/HookCounter'
import HookCounter2 from './components/HookCounter2'
import HookCounter3 from './components/HookCounter3'
import HookCounter4 from './components/HookCounter4'
export default function App() {
    return (
        <div>
            <HookCounterOne />

        </div>
    )
}
/**
 * !  Summary -  useState
 * !  1. The useState hook lets you add state to fucntional components
 * !  2. In classes, the state is always an object
 * !  3. With the useState hook, the state doesn't have to be an object
 * !  4. The useState hook returns an array with 2 elements
 * !       The first element is the current value of the state,
 * !      The second element is a state setter function
 * !  5. New state value depends on the preivous state value? you can pass a function to the setter function
 * !  6. When dealing with the objects and arrays, always make sure to spread your state variable then call the setter function
 */

// stop at use effect
// 
// https://www.youtube.com/watch?v=06Y6aJzTmXY&list=PLC3y8-rFHvwisvxhZ135pogtX7_Oe3Q3A&index=6  