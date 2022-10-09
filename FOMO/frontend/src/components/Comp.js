import React, { useState } from 'react'
import { Rating } from 'react-simple-star-rating'
import "./Comp.css";



export const Comp = (props) => {
  const [rating, setRating] = useState(0) // initial rating value


  const handleRating = (rate: number) => {
    setRating(rate)
  }

 return (
    <div className = "flex">
      <Rating  ratingValue={rating} readonly = 'true' initialValue={props.rating} showTooltip
 /* Available Props */ />
    </div>
  )
}