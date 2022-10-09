import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { chadwick, kilburn, mecd, uniplace, alang } from './imageSlice'

import KilburnIMG from '../images/profileKilburn.png'


export function ProfilePictureSelect() {
  const dispatch = useDispatch()

  return (
    <ul className='selection'>
      <li>
        <img className='profilepictureselect'
          src={KilburnIMG}
          onClick={() => dispatch(kilburn())}
        >
        </img>
      </li>

      <li>
        <img className='profilepictureselect'
          src={KilburnIMG}
          onClick={() => dispatch(mecd())}
        >
        </img>
      </li>
      <li>
        <img className='profilepictureselect'
          src={KilburnIMG}
          onClick={() => dispatch(chadwick())}
        >
        </img>
      </li>
      <li>
        <img className='profilepictureselect'
          src={KilburnIMG}
          onClick={() => dispatch(alang())}
        >
        </img>
      </li>
      <li>
        <img className='profilepictureselect'
          src={KilburnIMG}
          onClick={() => dispatch(uniplace())}
        >
        </img>
      </li>
    </ul>
  )
}