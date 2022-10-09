import React, {useEffect, useState} from 'react';
import FomoCal from '../components/FomoCal';
import Loader from '../components/Loader';
import NewUser from '../components/NewUser';



const Calendar = () => {
  const [events, setEvents] = useState([])
  const [auth, setAuth] = useState(false)
  const [newUser, setNewuser] = useState(false)
  const [loading, setLoading] = useState(false)

  const setIcs = () =>{
    setNewuser(()=>{
      return false
    })
  }

  const getWork = async()=>{
    try {
      var temp_events = []
      const res2 = await fetch('/api/jsonDeadlineEvents/')
      const data = await res2.json()
      if(data.length > 0){
        data.forEach(element => {
          if(element.start != null){
            var event  = {
              title: element.title,
              start: new Date(element.start),
              end: new Date(element.end),
              type: element.type,
              deadlineid: element.deadlineid,
              eventid: element.eventid,
              eventType: element.eventType,
              activityid: element.activityid
            }
            temp_events.push(event)
          }
        });
      }
      setEvents((prevEvents)=>{
        return [...prevEvents, ...temp_events]
      })
    } catch (err) {
      console.error("Error:",err)
    }
  }

  const getActivities = async()=>{
    try {
      var temp_events = []
      const res2 = await fetch('/api/jsonActivityEvents/')
      const data = await res2.json()
      if(data.length > 0){
        data.forEach(element => {
          if(element.start != null){
            var event  = {
              title: element.title,
              start: new Date(element.start),
              end: new Date(element.end),
              type: element.type,
              deadlineid: element.deadlineid,
              eventid: element.eventid,
              eventType: element.eventType,
              activityid: element.activityid,
              notes: element.notes,
              location: element.location,
            }
            temp_events.push(event)
          }
        });
      }
      setEvents((prevEvents)=>{
        return [...prevEvents, ...temp_events]
      })
    } catch (err) {
      console.error("Error:",err)
    }
  }

  const createWork = async()=>{
    try{
      setLoading(true)
      const res = await fetch('/api/createDeadlineEvents/')
      getWork()
      setLoading(false)
    }catch(err){
      console.error("Error:",err)
    }
  }

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

  const getEvents = async() =>{
    try {
      var temp_events = []
      const res = await fetch('/api/getEvents/')
      const data = await res.json()
      data.forEach(element => {
        if(element.start != null){
          var event  = {
            title: element.title,
            start: new Date(element.start),
            end: new Date(element.end),
            notes: element.notes,
            type: element.eventType,
          }
          temp_events.push(event)
        }
      });
      
      setEvents((prevEvents)=>{
        return [...prevEvents, ...temp_events]
      })
      
    } catch (err) {
      console.error("Error:",err)
    }
  }

  const getDeadlines = async() =>{
    try {
      var temp_events = []
      const res = await fetch('/api/jsonDeadlines/')
      const data = await res.json()
      data.forEach(element => {
        if(element.date_due != null){
          var end = new Date(element.date_due)
          end.setHours(end.getHours() + 1)
          var event  = {
            id : element.id,
            moduleid : element.moduleid,
            title: element.title,
            type: element.type,
            start: new Date(element.date_due),
            end: end,
            notes: (element.summative == "F" ? "Formative": "Summative"),
            type: "Deadline",
          }
          temp_events.push(event)
        }

      });
      setEvents((prevEvents)=>{
        return [...prevEvents, ...temp_events]
      })
    } catch (err) {
      console.error("Error:",err)
    }
  }

    useEffect(()=>{
      setEvents(()=>{
        return []
      })
      login()


      if(auth == false){
        checkIcs()
      }

      if(auth == false && newUser == false){
        getEvents()
        getDeadlines()
        getWork()
        getActivities()
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
            <NewUser noIcs={setIcs} createWork={createWork}/>
          </div>
      </div>
  );
  }
  else if(auth == false && newUser == false){
    return(
      <div className='contain'>
        <div className='calHeader'>
          <h2>Calendar</h2>
          <button onClick={createWork}>Create Work Slots</button>
        </div>
          <div className="panel">
            {events.length != 0? <FomoCal events={events}/> : <Loader/>}
          </div>
      </div>
  );
  }
    
};

export default Calendar;
