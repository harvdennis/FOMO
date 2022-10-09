import React, {useEffect, useState} from 'react';
import { BasicTable } from '../components/BasicTable';
import { deadlineTable } from '../components/deadlineTable';
import Loader from '../components/Loader';
import NewUser from '../components/NewUser';

const About = () => {
  const [auth, setAuth] = useState(false)
  const [newUser, setNewuser] = useState(false)
  const [loading, setLoading] = useState(false)

  const login = async()=>{
    try{
      const res = await fetch('/api/login/')
      const data = await res.json()
      if(data.url){
        setAuth(data.url)
      }else{
        setAuth(false)
      }
    }catch(err){
      console.error("Error:",err)
    }
  } 

  const checkIcs = async()=>{
    try {
      const res = await fetch('/api/checkIcs/')
      const data = await res.json()
      if(!data.valid){
        setNewuser(()=>{
          return true
        })
      }else{
        setNewuser(()=>{
          return false
        })
      }
    } catch (err) {
      console.error("Error:",err)
    }
  }

  useEffect(()=>{
    
    login()


    if(auth == false){
      checkIcs()
    }
    //Have a fetch call to check if the user ics exists

  },[])
  
  if(auth){
    console.log(auth)
    window.location.href = auth
  }
  else if(loading){
    return(
      <div className='contain'>
          <div className="panel">
            <Loader/>
          </div>
      </div>
  );
  }
  else if(newUser != false){
    return(
      <div className='contain'>
          <h2>Please upload your Calendar</h2>
          <div className="panel">
            <NewUser/>
          </div>
      </div>
  );
  }
  else if(auth == false && newUser == false){
    return(
      <div className='contain'>
          <h2>About Us</h2>
          <div className="panel">
            <BasicTable/>
            <deadlineTable/>
          </div>
      </div>
  );
  }
};

export default About;

