import React, {useState} from 'react'


const NewUser = (props) => {
    const [link, setLink] = useState(()=>{
        return('')
      })

    const [days, setDays] = useState([true,true,true, true, true,true,true])
    const [times, setTimes] = useState(["09:00", "17:00"])
    const [breakTime, setBreakTime] = useState(15)
    const [finish, setFinish] = useState(1)
    const [maxEvents, setMaxEvents] = useState(3)

    const changeLink = (e)=>{
        setLink(()=>{
            return(e.target.value)
        })
    }

    const handleSubmit = async() =>{
        var payload = {
            available_days: days,
            available_hours: times,
            ics_file: link,
            break_time: breakTime,
            max_sub_deadline_events_per_day: maxEvents,
            finish_days_before: finish
        }
        const settings = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        };

        try {
            const fetchResponse = await fetch(`http://localhost:3000/api/saveUserDetails/`, settings);
            const data = await fetchResponse
            if(data.status == 200){
                props.noIcs()
            }
            window.location.href = "http://localhost:3000/Calendar/"
            return data;
        } catch (e) {
            window.location.href = "http://localhost:3000/Calendar/"
            console.log(e)
            return e;
        }

    }

    const handleOnCheck = (e) =>{
        setDays(()=>{
            if(e.target.name === "Monday"){
                var copy = [...days]
                copy[0] = !days[0]
                return copy
            }
            else if(e.target.name === "Tuesday"){
                var copy = [...days]
                copy[1] = !days[1]
                return copy
            }
            else if(e.target.name === "Wednesday"){
                var copy = [...days]
                copy[2] = !days[2]
                return copy
            }
            else if(e.target.name === "Thursday"){
                var copy = [...days]
                copy[3] = !days[3]
                return copy
            }
            else if(e.target.name === "Friday"){
                var copy = [...days]
                copy[4] = !days[4]
                return copy
            }
            else if(e.target.name === "Saturday"){
                var copy = [...days]
                copy[5] = !days[5]
                return copy
            }
            else if(e.target.name === "Sunday"){
                var copy = [...days]
                copy[6] = !days[6]
                return copy
            }else{
                return days
            }
        })
    }

    const handleOnChange = (e) =>{
        setTimes(()=>{
            if(e.target.name === "Monday-time-start"){
                var copy = [...times]
                copy[0] = e.target.value
                return copy
            }
            
            else if(e.target.name === "Monday-time-end"){
                var copy = [...times]
                copy[1] = e.target.value
                return copy
            }
            else{
                return times
            }
        })

        if(e.target.name === 'breaktime'){
            setBreakTime(()=>{
                    return e.target.value
                
            })
        }

        if(e.target.name === 'finish' && e.target.value >= 1){
            setFinish(()=>{
                    return e.target.value
                
            })
        }

        if(e.target.name === 'maxEvents'){
            setMaxEvents(()=>{
                    return e.target.value
                
            })
        }
    }

  return (
    <div className='newUser'>
        <h2>Instructions:</h2>
        <h4>Click the link at the bottom and login to get see your timetable.</h4>
        <h4>In the top right of the page click SUBSCRIBE.</h4>
        <h4>At the bottom of the panel click More...</h4>
        <h4>Copy the link provided and paste it into the form below.</h4>
        <a href="https://timetables.manchester.ac.uk/" target="_blank"><h3>Get My Timetable</h3></a>
        <div className='formz'>
            <input className="ics-input" type="text" placeholder='Timetable Url' value={link} onChange={changeLink}/>
            <br />
            <h3>Please choose days you want to work</h3>
            <div className='day-check'>
                <input type="checkbox" name="Monday" id="Monday" onChange={handleOnCheck} checked={days[0]}/>
                <label htmlFor="Monday">Monday</label>
                <br />
                <input type="checkbox" name="Tuesday" id="Tuesday" onChange={handleOnCheck} checked={days[1]}/>
                <label htmlFor="Tuesday">Tuesday</label>
                <br />
                <input type="checkbox" name="Wednesday" id="Wednesday" onChange={handleOnCheck} checked={days[2]}/>
                <label htmlFor="Wednesday">Wednesday</label>
                
                <br />
                <input type="checkbox" name="Thursday" id="Thursday" onChange={handleOnCheck} checked={days[3]}/>
                <label htmlFor="Thursday">Thursday</label>
                
                <br />
                <input type="checkbox" name="Friday" id="Friday" onChange={handleOnCheck} checked={days[4]}/>
                <label htmlFor="Friday">Friday</label>
                
                <br />
                <input type="checkbox" name="Saturday" id="Saturday" onChange={handleOnCheck} checked={days[5]}/>
                <label htmlFor="Saturday">Saturday</label>
               
                <br />
                <input type="checkbox" name="Sunday" id="Sunday" onChange={handleOnCheck} checked={days[6]}/>
                <label htmlFor="Sunday">Sunday</label>
                
            </div>
            <div className='day-check-right'>
                    <h3>Choose the time you want to work between</h3>
                    <br />
                    <label htmlFor="Monday-time-start">Start</label>
                    <input type="time" name="Monday-time-start" id="Monday-time-end" value={times[0]} onChange={handleOnChange} />
                    <label htmlFor="Monday-time-end">End</label>
                    <input type="time" name="Monday-time-end" id="Monday-time-end" value={times[1]} onChange={handleOnChange}/>
                </div>
            <br />
            <div className='day-check'>
                <h3>Extra info</h3>
                <label htmlFor="breaktime">Break between work slots (in minutes):</label>
                <div className='day-check-right'>
                    <input type="number" name="breaktime" value={breakTime} onChange={handleOnChange} />
                </div>
                <br />
                <label htmlFor="finish">Days you want to finish before assignment:</label>
                <div className='day-check-right'>
                    <input type="number" name="finish" value={finish} onChange={handleOnChange} />
                </div>
                <br />
                <label htmlFor="maxEvents">Preffered time to spend on each deadline per day (hours):</label>
                <div className='day-check-right'>
                    <input type="number" name="maxEvents" value={maxEvents} onChange={handleOnChange} />
                </div>
                <br />
            </div>
            <button onClick={handleSubmit}>Submit</button>
        </div>
    </div>
  )
}

export default NewUser
