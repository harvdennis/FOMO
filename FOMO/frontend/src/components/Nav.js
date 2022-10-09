import React from 'react'
import {Link} from 'react-router-dom'


const Nav = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/"><img src={'/icons/Logo.svg'} alt="fomo"/></Link></li>
                <div class="non-home">
                    <li><Link  to="/About"><img src={'/icons/ratings.svg'} alt="rat"/></Link></li>
                    <li><Link  to="/Calendar"><img src={'/icons/calendar.svg'} alt="Cal"/></Link></li>
                    <li><Link  to="/Deadlines"><img src={'/icons/deadlines.svg'} alt="Dea"/></Link></li>
                    <li><Link  to="/Profile"><img src={'/icons/person.svg'} alt="pro"/></Link></li>
                </div>
            </ul>
        </nav>
    )
}

export default Nav
