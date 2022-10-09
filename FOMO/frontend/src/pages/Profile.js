import React, { Component, useEffect, useState } from 'react';
import Popup from 'reactjs-popup'
import ProfilePU from '../components/profilePopup'
import ThemePU from '../components/profileThemePopup'
import LogoutPU from '../components/profileLogoutPopup'
import { ProfilePictureOutput } from '../components/ProfilePictureOutput';
import NewUser from '../components/NewUser';
import Loader from '../components/Loader';
import useLocalStorage from 'use-local-storage'
import { useSelector, useDispatch } from 'react-redux';



const Profile = () => {
  const [auth, setAuth] = useState(false)
  const [newUser, setNewuser] = useState(false)
  const [loading, setLoading] = useState(false)
  const [userData, setUserData] = useState(true)

  const theme = useSelector((state) => state.theme.value)
  const dispatch = useDispatch()

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

  const getDetails = async()=>{
    try {
      const res = await fetch('/api/jsonUserDetails/')
      const data = await res.json()
      setUserData(data)
    } catch (err) {
      console.log('Error:', err)
    }
  }

  useEffect(()=>{
    
    login()


    if(auth == false){
      checkIcs()
    }

    if(auth=== false && newUser=== false && userData){
      getDetails()
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
  else if(auth == false && newUser == false) {
    return (
        <div className='contain'>
          <h2>Profile</h2>
          <div className="panel" id='panelsize'>
            <div className='panelcontent'>
              <div className='profile'>
                <div className='circle'>
                  <ProfilePictureOutput />
                </div>
                <p id='username'>{userData.fullname}</p>
                <p id='email'>{userData.username}</p>
              </div>
              <div>
                <ProfilePU />
              </div>
              <div>
                <ThemePU />
              </div>
              <div>
                <LogoutPU />
              </div>
            </div>
          </div>
        </div>
    );
  }
};

export default Profile;
