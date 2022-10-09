import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { kilburn, mecd } from './imageSlice'

export function ProfilePictureOutput() {
    const image = useSelector((state) => state.image.value)
    const dispatch = useDispatch()

    return (
            <img className='profilepicture' src={image}></img>
    )
}