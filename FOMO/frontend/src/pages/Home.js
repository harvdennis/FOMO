import React from 'react';

const Home = () => {
  return (
    <div className='bodyHomeOverride'>
      <div className='tophome'>
        <div>
          <img src={'/homeFOMO.png'} alt="FOMO Logo" className='images' style={{ position: "absolute", right: 0, bottom: 0 }} />
        </div>
        <div className='texthome'>
          <p className="t1">
            Welcome to
          </p>
          <p className="t2">
            FOMO
          </p>
          <p className="t3">
            {`
          Your assignments and
          deadlines, in one place.
          `}
          </p>
          <p className="t3">
            {`
          Plan better
          Work smarter
          Achive higher
          `}
          </p>
        </div>
      </div>

      <div className='midhome'>
        <img src={'/homeGitlab.png'} alt="Gitlab Logo" className='images' style={{ position: "absolute", right: 0, top: 0 }} />
        <img src={'/homePerson.png'} alt="Person Logo" className='images' style={{ position: "absolute", left: 0, bottom: 0 }} />
        <div className='textgrid'>
          <p className="m1">Never</p>
          <p className="m2">Miss,</p>
          <p className="m3">Always</p>
          <p className="m4">Deliver</p>
        </div>
      </div>

      <div className='bottomhome'>
        <div className='dashedsquare'>
          <p className='b1'>Register Now!</p>
          <p className='b2'>
            You will need your University of Manchester email to verify you are a student to use this service.<br />
            <br />
            From there, you will able to import all your deadlines from Blackboard.
          </p>
          <a href="/Calendar/">
            <img src={'/homeSignup.png'} alt="Gitlab" />
          </a>
        </div>
      </div>
    </div>
  );
}

export default Home;
