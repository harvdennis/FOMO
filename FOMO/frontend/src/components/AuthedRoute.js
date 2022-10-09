import React, {useEffect, useState} from 'react'
import { Route, Navigate } from 'react-router-dom';


const AuthedRoute = ({component: Component, ...rest}) => {
    const [auth, setAuth] = useState(false)
    useEffect(()=>{
      fetch('http://localhost:8000/login/').then(res =>{
        console.log(res)
      }).catch(err=>{
        console.error("Error:",err)
      })
    },[])
  return (
    <Route {...rest} render={(props) => (auth === false ? <Navigate to="https://google.com" /> : <Component {...props} />)}/>
  )
}

export default AuthedRoute