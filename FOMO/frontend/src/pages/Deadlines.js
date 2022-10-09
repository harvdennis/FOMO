import React, { useEffect, useState } from "react";

import { BasicTable } from "../components/deadlineTable";
import Loader from "../components/Loader";
import NewUser from "../components/NewUser";

const Deadlines = () => {
  const [auth, setAuth] = useState(false);
  const [newUser, setNewuser] = useState(false);
  const [loading, setLoading] = useState(false);
  const [events, setEvents] = useState([]);

  const login = async () => {
    try {
      const res = await fetch("/api/login/");
      const data = await res.json();
      if (data.url) {
        setAuth(data.url);
      } else {
        setAuth(false);
      }
    } catch (err) {
      console.error("Error:", err);
    }
  };

  const checkIcs = async () => {
    try {
      const res = await fetch("/api/checkIcs/");
      const data = await res.json();
      if (!data.valid) {
        setNewuser(() => {
          return true;
        });
      } else {
        setNewuser(() => {
          return false;
        });
      }
    } catch (err) {
      console.error("Error:", err);
    }
  };

  const getDeadlines = async () => {
    try {
      var temp_events = [];
      var deadline_panels = [];
      const res = await fetch("/api/jsonDeadlines/");
      const data = await res.json();
      const today = new Date();

      data.forEach((element) => {
        if (element.date_due != null) {
          var end = new Date(element.date_due);
          end.setHours(end.getHours() + 1);
          var event = {
            id: element.id,
            moduleid: element.moduleid,
            title: element.title,
            type: element.type,
            start: new Date(element.date_due),
            end: end,
            notes: element.summative == "F" ? "Formative" : "Summative",
            type: "Deadline",
          };
          temp_events.push(event);
        }
      });

      const sortedEvents = temp_events.sort((a, b) => a.start - b.start);
      console.log(temp_events);
      sortedEvents.forEach((element) => {
        if (element.start > today) {
          // deadline_panels.push(
          //   <div className='label'>
          //     <h3>{element.title}</h3>
          //     <h4>Course: {element.moduleid}</h4>
          //     <h4>{element.notes}</h4>
          //     <h4>Due: {element.start.toLocaleDateString()}</h4>
          //   </div>
          // )
          deadline_panels.push({
            id: element.id,
            title: element.title,
            end: element.start.toLocaleDateString(),
          });
        }
      });
      setEvents((prevEvents) => {
        return deadline_panels;
      });
    } catch (err) {
      console.error("Error:", err);
    }
  };

  useEffect(() => {
    setEvents(() => {
      return [];
    });
    login();

    if (auth == false) {
      checkIcs();
    }

    if (auth == false && newUser == false) {
      getDeadlines();
    }

    //Have a fetch call to check if the user ics exists
  }, []);

  if (auth) {
    console.log(auth);
    window.location.href = auth;
  } else if (loading) {
    return (
      <div className="contain">
        <div className="panel">
          <Loader />
        </div>
      </div>
    );
  } else if (newUser != false) {
    return (
      <div className="contain">
        <h2>Please upload your Calendar</h2>
        <div className="panel">
          <NewUser />
        </div>
      </div>
    );
  } else if (auth == false && newUser == false) {
    return (
      <div className="contain">
        <h2>Upcoming Deadlines</h2>
        <div className="panel" id="panelsize">
          <div>
            <BasicTable deadlines={events} />
            {/* <h2>Upcoming Deadlines</h2>
          <div className='panel'>
            {events}
          </div> */}
          </div>
        </div>
      </div>
    );
  }
};

export default Deadlines;
