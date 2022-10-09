import React, {useState, useEffect} from 'react';
import { Calendar, momentLocalizer  } from 'react-big-calendar' 
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import 'react-big-calendar/lib/css/react-big-calendar.css';
import '../calendar.css'
import moment from 'moment'


//start the week on a monday
moment.locale('ko', {
  week: {
      dow: 1,
      doy: 1,
  },
});

const localizer = momentLocalizer(moment)
const DndCalendar = withDragAndDrop(Calendar)

const FomoCal = (props) => {

  const [events, setEvents] = useState(() =>{
    return props.events
  })

  const[deadlines, setDeadlines] = useState([])
  const[activities, setActivities] = useState([])

  const [seen, setSeen] = useState(()=>{
    return "none"
  })

  const [popUpPos, setPopUp] = useState(()=>{
    return{x: 0, y: 0}
  })

  const [time, setTime] = useState(()=>{
    return{start: "12:00", end: "13:00"}
  })

  const [title, setTitle] = useState(()=>{
    return('')
  })

  const [eventIndex, setEventIndex] = useState(()=>{
    return(0)
  })

  const [clickCount, setClickCount] = useState(()=>{
    return 1
  })

  const [notes, setNotes] = useState(false)
  const [location, setLocation] = useState(false)
  const [moduleid, setModuleid] = useState(false)
  const [type, setType] = useState('')

  const submitActivities = async(updated) =>{
    
    let payload = []
    updated.forEach((element)=>{
      if(typeof(element.start) !== 'string' || typeof(element.end) !== 'string'){
        const format_start = element.start.toISOString()
        const format_end = element.end.toISOString()
        let data = {...element}
        data.start = format_start
        data.end = format_end
        payload.push(data)
      }
    })

    const settings = {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
    };

    try {
        const fetchResponse = await fetch(`/api/activitesUpdate/`, settings);
        const data = await fetchResponse.json()
        console.log(data)
          
        return data;
    } catch (e) {
        console.log(e)
        return e;
    }
   
  }

  const submitDeadlines = async(updated) =>{

    let payload = []
    updated.forEach((element)=>{
      if(typeof(element.start) !== 'string' || typeof(element.end) !== 'string'){
        const format_start = element.start.toISOString()
        const format_end = element.end.toISOString()
        let data = {...element}
        data.start = format_start
        data.end = format_end
        payload.push(data)
      }
    })

    const settings = {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
    };

    try {
        const fetchResponse = await fetch(`/api/deadlineEventsUpdate/`, settings);
        const data = await fetchResponse.json()
        console.log(data)
        
        return data;
    } catch (e) {
        console.log(e)
        return e;
    }

  }

  useEffect(()=>{
    const tempDeadlines = []
    const tempActivities = []
    setEvents(props.events)
    props.events.forEach(element=>{
      if(element.eventType === 'deadline'){
        tempDeadlines.push(element)
      }
      if(element.eventType === 'activity'){
        tempActivities.push(element)
      }
    })

    setDeadlines(tempDeadlines)
    setActivities(tempActivities)

  },[props.events])

  useEffect(()=>{
    const submitUpdates = setTimeout(() => {
      console.log(activities)
      submitActivities(activities)
    }, 3000);

    return () => clearTimeout(submitUpdates)

  },[activities])

  useEffect(()=>{
    const submitUpdates = setTimeout(() => {
      submitDeadlines(deadlines)
    }, 3000);

    return () => clearTimeout(submitUpdates)

  },[deadlines])

  const styleEvent = (event, start, end, isSelected) =>{
    var backgroundColor = '#2b9137d2'

    if(event.type == 'attendance'){
      backgroundColor = '#6c2b91d2'
    }
    else if(event.type == 'Deadline'){
      backgroundColor = '#961818d2'
    }
    else if(event.type == 'Lab'){
      backgroundColor = '#2b3c91d2'
    }
    else if(event.type === 'Essay'){
      backgroundColor = '#964b18d2'
    }
    else if(event.type === 'Worksheet'){
      backgroundColor = '#189655d2'
    }
    else if(event.type === 'Coursework'){
      backgroundColor = '#967b18d2'
    }
    var style = {
        backgroundColor: backgroundColor,
    };
    return {
        style: style
    };
  }

  const handleAdd = ({ start, end }) => {

    if(clickCount === 2){
      setSeen(()=>{
        return ("block")
      })
      setEvents(prevEvents => {
        return [
          ...prevEvents,
          {
            title,
            start,
            end,
            type: "Activity",
            eventType: "activity",
            eventid: prevEvents.length,
            activityid: 0,
            notes: '',
            location: '',
          }
        ]
      })

      setActivities(prevEvents => {
        return [
          ...prevEvents,
          {
            title,
            start,
            end,
            type: "Activity",
            eventType: "activity",
            eventid: events.length,
            activityid: 0,
            deadlineid:0,
            notes: '',
            location: '',
          }
        ]
      })



      setTime(()=>{
        return {start: moment(start).format("HH:mm"), end: moment(end).format("HH:mm")}
      })

      setEventIndex(()=>{
        return events.length
      })

      setClickCount((prevClick)=>{
        return(0)
      })

      setModuleid(()=>{
        return false
      })

      setNotes(()=>{
        return false
      })

      setLocation(()=>{
        return false
      })
       
      setType(()=>{
         return 'Activity'
      })
    }
  }

  const moveEvent = ({ event, start, end }) =>{
    if(event.type !== "Deadline" && event.type !== "attendance"){

      const index = events.indexOf(event);
      const updatedEvent = { ...event, start, end };

      const nextEvents = [...events];
      nextEvents.splice(index, 1, updatedEvent);

      if(event.eventType === 'activity'){
        const activityIndex = activities.indexOf(event);
        const updatedActivity = { ...event, start, end };

        const nextActivities = [...activities];
        nextActivities.splice(activityIndex, 1, updatedActivity);

        setActivities(()=>{
          return nextActivities
        })
      }

      if(event.eventType === 'deadline'){
        const deadlineIndex = deadlines.indexOf(event);
        const updatedDeadline = { ...event, start, end };

        const nextDeadlines = [...deadlines];
        nextDeadlines.splice(deadlineIndex, 1, updatedDeadline);


        setDeadlines(()=>{
          return nextDeadlines
        })
      }

      setEvents(()=>{
        return nextEvents
      });

  }


  }

  const getMousePos = (e) =>{
    if(e.target.id !== 'cal_popup' && e.target.id !== 'cal_popup-input'){
      setSeen(()=>{
        return ("none")
      })

      setPopUp(()=>{
        return{x: e.clientX, y: e.clientY}
      })

      setTitle(()=>{
        return('New event')
      })
    }

    if(e.target.className === 'rbc-events-container' || e.target.className === 'rbc-day-bg' || e.target.className === 'rbc-row'){
      setClickCount((prevClick)=>{
        return(prevClick === 2? 0: prevClick+1 )
      })
    }
  }

  const eventInfo = (e) =>{
    setSeen(prevSeen=>{
      return (prevSeen === "none"? "block": "none")
    })

    setTitle(()=>{
      return(e.title)
    })

    setTime(()=>{
      return({start: moment(e.start).format("HH:mm"), end: moment(e.end).format("HH:mm")})
    })

    setEventIndex(()=>{
      return events.indexOf(e)
    })

    setClickCount((prevClick)=>{
      return(0)
    })

    if(typeof e.moduleid !== 'undefined'){
      setModuleid(()=>{
        return e.moduleid
      })
    }else{
      setModuleid(()=>{
        return false
      })
    }

    if(typeof e.location !== 'undefined'){
      setLocation(()=>{
        return e.location
      })
    }else{
      setLocation(()=>{
        return false
      })
    }

    if(typeof e.notes !== 'undefined'){
      setNotes(()=>{
        return e.notes
      })
    }else{
      setNotes(()=>{
        return false
      })
    }

    if(typeof e.type !== 'undefined'){
      setType(()=>{
        return e.type
      })
    }else{
      setType(()=>{
        return false
      })
    }

  }

  const changeEnd = (e) =>{
    if(type !== "Deadline" && type !== "attendance"){
      setTime((prevTime)=>{
        return({start: prevTime.start, end: e.target.value})
      })
  
      const event = events[eventIndex]
      const updatedEvent = { ...event, end: moment(event.end).set({'hour': Number(e.target.value.substr(0,2)), 'minute': Number(e.target.value.substr(3,4))}) };
  
      const nextEvents = [...events];
      nextEvents.splice(eventIndex, 1, updatedEvent);

      if(event.eventType === 'activity'){
        const activityIndex = activities.indexOf(event);
        const updatedActivity = { ...event, end: moment(event.end).set({'hour': Number(e.target.value.substr(0,2)), 'minute': Number(e.target.value.substr(3,4))})};

        const nextActivities = [...activities];
        nextActivities.splice(activityIndex, 1, updatedActivity);

        setActivities(()=>{
          return nextActivities
        })
      }

      if(event.eventType === 'deadline'){
        const deadlineIndex = deadlines.indexOf(event);
        const updatedDeadline = { ...event, end: moment(event.end).set({'hour': Number(e.target.value.substr(0,2)), 'minute': Number(e.target.value.substr(3,4))}) };

        const nextDeadlines = [...deadlines];
        nextDeadlines.splice(deadlineIndex, 1, updatedDeadline);


        setDeadlines(()=>{
          return nextDeadlines
        })
      }
  
      setEvents(()=>{
        return nextEvents
      });
    }
  }

  const changeTitle = (e)=>{
    if(type !== "Deadline" && type !== "attendance"){
      setTitle(()=>{
        return(e.target.value)
      })
      const event = events[eventIndex]
      const updatedEvent = { ...event, title: e.target.value };
  
      const nextEvents = [...events];
      nextEvents.splice(eventIndex, 1, updatedEvent);

      if(event.eventType === 'activity'){
        const activityIndex = activities.indexOf(event);
        const updatedActivity = { ...event, title: e.target.value};

        const nextActivities = [...activities];
        nextActivities.splice(activityIndex, 1, updatedActivity);

        setActivities(()=>{
          return nextActivities
        })
      }

      if(event.eventType === 'deadline'){
        const deadlineIndex = deadlines.indexOf(event);
        const updatedDeadline = { ...event, title: e.target.value};

        const nextDeadlines = [...deadlines];
        nextDeadlines.splice(deadlineIndex, 1, updatedDeadline);


        setDeadlines(()=>{
          return nextDeadlines
        })
      }
  
      setEvents(()=>{
        return nextEvents
      });
    }
  }

  const deleteEvent = () =>{
    if(type === 'Activity'){
      const nextEvents = [...events];
      nextEvents.splice(eventIndex, 1);

      if(events[eventIndex].eventType === 'activity'){
        const activityIndex = activities.indexOf(events[eventIndex]);

        const nextActivities = [...activities];
        nextActivities.splice(activityIndex, 1);
        
        setActivities(()=>{
          return nextActivities
        })
      }

      setEvents(()=>{
        return nextEvents
      });
      setSeen(()=>{
        return ("none")
      })
      setClickCount((prevClick)=>{
        return(1)
      })
  }
  }

  return (
    <div onMouseDown= {getMousePos}>
      <div id="cal_popup" style={{"display":`${seen}`, "top":`${popUpPos.y}px`, "left": `${popUpPos.x + 10}px`}}>
        <input id="cal_popup-input" type="text" name="new_event" placeholder='New Event' value={title} onChange={changeTitle}/>
        <input id="cal_popup-input" type="time" name="start_time" value={time.start}/>
        <input id="cal_popup-input" type="time" name="end_time" value={time.end} onChange={changeEnd}/>
        <div className='extra-info'>
          {moduleid ? (<p>Module: {moduleid}</p>): null}
          {notes ? (<p>Notes: {notes}</p>): null}
          {location ? (<p>Location: {location}</p>): null}
          {type ? (<p>Type: {type}</p>): null}
        </div>
        <button id="cal_popup-input" onClick={deleteEvent}>Delete</button>
      </div>
      <DndCalendar
        selectable
        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
        views={['month', 'week', 'day']}
        style = {{minHeight: '500px', height: "90vh"}}
        onSelectEvent={eventInfo}
        onEventDrop={moveEvent}
        resizable
        onSelectSlot={handleAdd}
        defaultView='week'
        scrollToTime= {moment()}
        eventPropGetter={styleEvent}
      />
    </div>
  );
};

export default FomoCal;
